#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# author mengskysama

from flask import Blueprint, render_template, abort, g, url_for, redirect
from flask.ext.login import login_required
from jinja2 import TemplateNotFound
from web.models import Beatmap
from web import app, db
from datetime import datetime


beatmap_page = Blueprint('beatmap_page', __name__, template_folder='templates', url_prefix='/beatmap')

@beatmap_page.route('/')
def beatmap_list_show():
    beatmaps = Beatmap.query.order_by(Beatmap.date.desc()).limit(100).all()
    for beatmap in beatmaps:
        pos = beatmap.title.find('(')
        if pos != -1:
            beatmap.title = beatmap.title[:pos]
    return render_template('beatmap/list.html', beatmaps=beatmaps)
