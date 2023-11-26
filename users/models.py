
from .. import db

from typing import List
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import relationship
class User(db.Model):
    __tablename__ = "users_table"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    name = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(32), nullable=False)
    specialty = db.Column(db.String(32), nullable=False)
    working_area = db.Column(db.String(32), nullable=False)
    dashboards: Mapped[List["Dashboard"]] = relationship()


    def __repr__(self):
        return '<User %r>' % self.username