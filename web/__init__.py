#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# author mengskysama

from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.login import LoginManager


app = Flask(__name__)
app.config.from_object('config')
app.secret_key = app.config.get('SECRET_KEY')

# database
db = SQLAlchemy(app)
from web import models

# login manager
login_manager = LoginManager()
login_manager.setup_app(app)
login_manager.login_view = 'login'

# views
#from web import views
# from web.views.login import simple_page
# app.register_blueprint(simple_page)

#from views.ticket import ticket_page
#from views.statistics import statistics_page

#app.register_blueprint(ticket_page)
#app.register_blueprint(statistics_page)

from views.beatmap import beatmap_page
app.register_blueprint(beatmap_page)