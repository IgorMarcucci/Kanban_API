from .. import db
from typing import List
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import relationship

class Dashboard(db.Model):
    __tablename__ = "dashboards_table"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    tickets: Mapped[List["Ticket"]] = relationship()

    def __repr__(self):
        return '<Dashboard %r>' % self.username