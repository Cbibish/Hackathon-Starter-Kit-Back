from sqlalchemy import Column, String, Integer, func, DateTime, Text

from shared import db


class eventsModel(db.Model):
    __tablename__ = "events"
    id = Column(
        Integer,
        primary_key=True,
        unique=True,
        nullable=False
    )
    Titre=Column(String(255))
    description=Column(String(255))
    foto=Column(Text)
    time_created = Column(DateTime(timezone=True), server_default=func.now())
