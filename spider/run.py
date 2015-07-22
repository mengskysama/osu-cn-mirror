#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# author mengskysama

import time

from spider import SpiderBloodCat
from db import DbHelper
import logging
import config
from qiniu.qiniu_upload import UploadFileToken, UploadFile

logging.basicConfig(level=logging.INFO)
bucket = 'osu-cn-mirror'


def work():
    s = SpiderBloodCat()
    db = DbHelper()

    while True:
        try:
            ms = s.fetch()
            for m in ms:
                if db.is_duplicate(m.id, m.date) is False:
                    # if exsit download it
                    file_name = s.download(m.id)
                    # upload to qiniu
                    key = file_name
                    filename = file_name
                    uploadfiletoken = UploadFileToken(config.ACCESS_KEY, config.SECRET_KEY, bucket, key)
                    uploder = UploadFile(filename, key, uploadfiletoken.token)
                    uploder.upload()
                    # insert to db
                    db.insert(m)
        except:
            import traceback
            traceback.print_exc()
            db = DbHelper()
        time.sleep(60)


work()