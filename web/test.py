from web import db

from web.models import Beatmap
from datetime import datetime

def init_db():
    db.create_all()



#init_db()

print Beatmap.query.filter_by(id=1).all()

