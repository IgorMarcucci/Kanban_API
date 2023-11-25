from .. import db
from typing import List
from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column

class Ticket(db.Model):
    __tablename__ = "tickets_table"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    description = db.Column(db.String(300), nullable=False)
    dashboard_id: Mapped[int] = mapped_column(ForeignKey("dashboards_table.id"))