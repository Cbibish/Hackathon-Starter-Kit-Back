from sqlalchemy import Column, String, Integer

from shared import db


class votesModel(db.Model):
    __tablename__ = "votes"
    votes_id = Column(
        Integer,
        primary_key=True,
        unique=True,
        nullable=False
    )
    opt1=Column(String(255))
    opt2=Column(String(255))
    opt3=Column(String(255))
    opt4=Column(String(255))
    cnt1=Column(Integer)
    cnt2=Column(Integer)
    cnt3=Column(Integer)
    cnt4=Column(Integer)
