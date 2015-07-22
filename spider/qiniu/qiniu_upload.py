#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# author mengskysama

# for no ascii filename upload


import time
import json
from hashlib import sha1
from base64 import urlsafe_b64encode
import hmac
import config
from multipart_post import post_multipart
import binascii

def hmac_sha1_encode(data, secret_key):
    return urlsafe_b64encode(hmac.new(secret_key,
        data, sha1).digest())


class UploadFileToken():
    def __init__(self, access_key, secret_key, bucket, key):
        self.access_key = access_key
        self.secret_key = secret_key
        self.bucket = bucket
        self.key = key
        self._token = None
        self._made_token_time = int(time.time())
        self.ttl = 3600 * 24

    @property
    def token(self):
        if self._token is None or int(time.time() - self._made_token_time) < 60:
            self._made_token_time = int(time.time())
            self._token = self._make_token()
        return self._token

    def _make_token(self):
        put_policy = {
                'scope': self.bucket + ':' + self.key,
                'deadline': self._made_token_time + self.ttl
                }
        put_policy = json.dumps(put_policy)
        encoded_put_policy = urlsafe_b64encode(put_policy)
        encoded_sign = hmac_sha1_encode(encoded_put_policy, self.secret_key)
        return ':'.join([self.access_key, encoded_sign, encoded_put_policy])


class UploadFile():
    def __init__(self, filename, key, token):
        self.filename = filename
        self.key = key
        self.token = token

    def upload(self):
        fields = {'key': self.key, 'token': self.token}
        files = [{'filename': self.filename}]
        return post_multipart('upload.qiniu.com', '/', fields, files)

    def calc_crc32(self):
        buf = open(self.filename, 'rb').read()
        buf = (binascii.crc32(buf) & 0xFFFFFFFF)
        return "%08X" % buf


if __name__ == "__main__":
    key = 'パリジョナ大作戦'
    bucket = 'osu-cn-mirror'
    filename = 'パリジョナ大作戦.osz'

    uploadfiletoken = UploadFileToken(config.ACCESS_KEY, config.SECRET_KEY, bucket, key)
    uploder = UploadFile(filename, key, uploadfiletoken.token)
    uploder.upload()
