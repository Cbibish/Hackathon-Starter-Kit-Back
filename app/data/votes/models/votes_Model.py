from sqlalchemy import Column, String, Integer

from shared import db


class votesModel(db.Model):
    __tablename__ = "votes"
    id = Column(
        Integer,
        primary_key=True,
        unique=True,
        nullable=False
    )
    message = Column(String(100))
