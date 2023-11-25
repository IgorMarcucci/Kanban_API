
from .. import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    name = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(32), unique=True, nullable=False)
    specialty = db.Column(db.String(32), unique=True, nullable=False)
    working_area = db.Column(db.String(32), unique=True, nullable=False)


    def __repr__(self):
        return '<User %r>' % self.username