from sqlalchemy import Column, String, Integer
from flask_login import UserMixin
from shared import db


class UserModel(db.Model):
    __tablename__ = "User"
    id = Column(Integer,primary_key=True,unique=True,nullable=False )
    username = Column(String(255)) 
    password = Column(String(255))
    email = Column(String(255))
    
