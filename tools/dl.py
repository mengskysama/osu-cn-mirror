#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# author mengskysama

import threadpool, threading
import time, random
import requests
import socket

socket.setdefaulttimeout(15)

l = threading.Lock()

r = open('e.txt', 'r').read(-1)
url = r.split('\n')


def h(r):

    while True:
        try:
            r = requests.get(r, timeout=60)
            file_name = r.headers['content-disposition']
            file_name = file_name[file_name.find('"')+1:-1]
            with open(file_name, 'wb') as d:
                d.write(r.content)
            return
            print 'ok'
        except:
            import traceback
            traceback.print_exc()
            pass



pool = threadpool.ThreadPool(1)
req = threadpool.makeRequests(h, url)
[pool.putRequest(req) for req in req]
pool.wait()