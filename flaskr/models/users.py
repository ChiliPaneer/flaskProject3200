from flaskr import db
from sqlalchemy import Table, MetaData, Column, Integer, String, TIMESTAMP, DATETIME, Enum
import datetime


class Users(db.Model):
    __tablename__ = 'users'
    id = db.Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    first_name = Column(String(45))
    last_name = Column(String(45))
    username = Column(String(45), nullable=False)
    password = Column(String(45), nullable=False)
    # TODO How to take in a datetime?
    date_of_birth = Column(DATETIME, default=datetime.datetime.now)
    created = Column(DATETIME, default=datetime.datetime.now)
    updated = Column(DATETIME, default=datetime.datetime.now, onupdate=datetime.datetime.now)
    email = Column(String(45), default="ex@mail.com")
