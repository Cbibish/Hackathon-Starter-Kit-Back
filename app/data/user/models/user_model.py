from sqlalchemy import Column, String, Integer

from shared import db


class UserModel(db.Model):
    __tablename__ = "User"
    id = Column(
        Integer,
        primary_key=True,
        unique=True,
        nullable=False
    )
    message = Column(String(100))

