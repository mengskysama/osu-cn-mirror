#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# author mengskysama

import httplib, mimetypes


def post_multipart(host, uri, fields, files):
    content_type, body = encode_multipart_formdata(fields, files)
    h = httplib.HTTPConnection(host)
    headers = {
        'User-Agent': 'wozhenderilegoule',
        'Content-Type': content_type
        }
    h.request('POST', uri, body, headers)
    res = h.getresponse()
    return res.status, res.reason, res.read() 


def encode_multipart_formdata(fields, files):
    """
    fields is a sequence of (name, value) elements for regular form fields.
    files is a sequence of (name, filename, value) elements for data to be uploaded as files
    Return (content_type, body) ready for httplib.HTTP instance
    """
    BOUNDARY = '---13222222222'
    CRLF = '\r\n'
    L = []
    for key in fields:
        L.append('--' + BOUNDARY)
        L.append('Content-Disposition: form-data; name="%s"' % key)
        L.append('')
        L.append(fields[key])
    for file in files:
        print file['filename']
        with open(file['filename'], 'rb') as f:
            data = f.read()
        L.append('--' + BOUNDARY)
        L.append('Content-Disposition: form-data; name="file"; filename="%s"' % (file['filename']))
        L.append('Content-Type: %s' % get_content_type(file['filename']))
        L.append('Content-Transfer-Encoding: binary')
        L.append('')
        L.append(data)
    L.append('--' + BOUNDARY + '--')
    L.append('')
    body = CRLF.join(L)
    content_type = 'multipart/form-data; boundary=%s' % BOUNDARY
    return content_type, body


def get_content_type(filename):
    return mimetypes.guess_type(filename)[0] or 'application/octet-stream'
