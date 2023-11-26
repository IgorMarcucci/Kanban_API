from .. import db
from typing import List
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import relationship
from sqlalchemy import ForeignKey
from sqlalchemy.orm import mapped_column

class Dashboard(db.Model):
    __tablename__ = "dashboards_table"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    tickets: Mapped[List["Ticket"]] = relationship()
    user_id: Mapped[int] = mapped_column(ForeignKey("users_table.id"))

    def __repr__(self):
        return '<Dashboard %r>' % self.username