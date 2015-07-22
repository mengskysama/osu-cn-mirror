#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# author mengskysama

from web import db


class Beatmap(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    artist = db.Column(db.String(256), nullable=False)
    title = db.Column(db.String(256), nullable=False)
    creator = db.Column(db.String(256), nullable=False)
    artistUnicode = db.Column(db.String(256), nullable=False)
    titleUnicode = db.Column(db.String(256), nullable=False)
    creatorId = db.Column(db.Integer, nullable=False)
    status = db.Column(db.Integer, nullable=False)
    date = db.Column(db.Integer, nullable=False)
    bpm = db.Column(db.Float, nullable=False)
    genre = db.Column(db.Integer, nullable=False)
    mode = db.Column(db.String(256), nullable=False)
    addtime = db.Column(db.Integer, nullable=False)
    count = db.Column(db.Integer, nullable=False)
    fork = db.Column(db.String(256), nullable=False)
    #file_name = db.Column(db.String(256), nullable=False)

    def __repr__(self):
        return '<Beatmap id=%r>' % (self.id)
