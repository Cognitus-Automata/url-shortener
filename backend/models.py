# from backend.database import db
from main import db

class Entry(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    url = db.Column(db.String, unique=True, nullable=False)
    short_url = db.Column(db.String)
