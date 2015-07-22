#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# author mengskysama

import requests
import json
import socket
import time
import logging

from datetime import datetime, timedelta

socket.setdefaulttimeout(15)
logging.getLogger("requests").setLevel(logging.WARNING)
logging.basicConfig(level=logging.INFO)


class BeatMap(object):

    id = None
    artist = None
    title = None
    creator = None
    artistUnicode = None
    titleUnicode = None
    creatorId = None
    status = None
    date = None
    bpm = None
    genre = None
    mode = None

    @staticmethod
    def load_from_json(j):
        m = BeatMap()
        for k in j:
            if j[k] is None:
                v = ''
            else:
                v = j[k].encode('utf-8')
                if k == 'date':
                    # fix korea to UTC
                    t_str = v[0:10] + ' ' + v[11:19]
                    d = datetime.strptime(t_str, '%Y-%m-%d %H:%M:%S') - timedelta(hours=9) + timedelta(hours=8)
                    v = int(time.mktime(d.timetuple()))
            if hasattr(m, k):
                setattr(m, k, v)
        return m


class SpiderBloodCat(object):

    @staticmethod
    def fetch(page=1):
        logging.info(('begin fetch page=%s' % page).decode('utf-8'))
        r = requests.get('http://bloodcat.com/osu/?mod=json&p=%s' % page).text
        j = json.loads(r)
        ms = []
        for j in j['results']:
            ms.append(BeatMap.load_from_json(j))
        return ms

    @staticmethod
    def download(id):
        logging.info(('begin download id=%s' % id).decode('utf-8'))
        r = requests.get('http://bloodcat.com/osu/s/%s' % id)
        file_name = r.headers['content-disposition']
        file_name = file_name[file_name.find('"')+1:-1]
        with open(file_name, 'wb') as d:
            d.write(r.content)
        return file_name
