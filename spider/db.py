#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# author mengskysama

import MySQLdb
import config
import time


class DbHelper(object):

    def __init__(self):

        self.conn = MySQLdb.connect(host=config.MYSQL_HOST, port=config.MYSQL_PORT,
                                    user=config.MYSQL_USER,passwd=config.MYSQL_PASS,
                                    db=config.MYSQL_DB, charset='utf8')

    def is_duplicate(self, id, date):
        cur = self.conn.cursor(cursorclass=MySQLdb.cursors.DictCursor)
        n = cur.execute('select * from beatmap where id=%s and date=%s' % (id, date))
        n = len(cur.fetchall())
        cur.close()
        if n == 0:
            return False
        return True

    def insert(self, beatmap):
        cur = self.conn.cursor()

        sql = "DELETE FROM `beatmap` WHERE id = %d" \
              "" \
              "'" \
              ""
        cur.execute(sql)
        sql = "INSERT INTO `beatmap` (`id`, `artist`, `title`, `creator`, " \
              "`artistUnicode`, `titleUnicode`, `creatorId`, `status`, " \
              "`date`, `bpm`, `genre`, `mode`, " \
              "`addtime`, `count`) VALUES (" \
              "'%s', '%s', '%s', '%s', " \
              "'%s', '%s', '%s', '%s', " \
              "'%s', '%s', '%s', '%s', " \
              "'%s', '%s')" % (beatmap.id, beatmap.artist, beatmap.title, beatmap.creator,
                               beatmap.artistUnicode, beatmap.titleUnicode, beatmap.creatorId, beatmap.status,
                               beatmap.date, beatmap.bpm, beatmap.genre, beatmap.mode,
                               int(time.time()), 0)
        cur.execute(sql)
        cur.close()
        self.conn.commit()

    def all(self):
        cur = self.conn.cursor(cursorclass=MySQLdb.cursors.DictCursor)
        n = cur.execute('select id from beatmap')
        r = cur.fetchall()
        f = open('e.txt', 'w')
        for i in r:
            f.write('http://bloodcat.com/osu/s/'+str(i['id']) + '\n')
        cur.close()
        f.close()

h = DbHelper()
h.all()