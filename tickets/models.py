from .. import db
from typing import List
from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column

class Ticket(db.Model):
    __tablename__ = "tickets_table"
    id = db.Column(db.String(128), primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    description = db.Column(db.String(300), nullable=False)
    dashboard_id: Mapped[str] = mapped_column(ForeignKey("dashboards_table.id"))

    def __repr__(self):
        return '<Ticket %r>' % self.name

    def toDict(self):
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description,
            "dashboard_id": self.dashboard_id
        }