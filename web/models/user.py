#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# author mengskysama

from web import db


class User(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    nickname = db.Column(db.String(64), unique=True, nullable=False)
    email = db.Column(db.String(64), unique=True, nullable=False)
    password = db.Column(db.String(32), nullable=False)
    role = db.Column(db.SmallInteger, default=0, nullable=False)

    def is_authenticated(self):
        if self.disable != 0:
            return False
        return True

    def is_active(self):
        if self.disable != 0:
            return False
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return unicode(self.id)

    def __repr__(self):
        return '<User %r>' % (self.nickname)