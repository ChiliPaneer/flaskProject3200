import enum
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import sessionmaker
import datetime

from sqlalchemy import Table, MetaData, Column, Integer, String, TIMESTAMP, DATETIME, Enum


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:P@ssw0rd@localhost/python_test'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = 'FALSE'


db = SQLAlchemy(app)


engine = create_engine(
    'mysql+pymysql://root:P@ssw0rd@localhost/python_test',
    echo=True
)
Session = sessionmaker(bind=engine)



class Users(db.Model):
    __tablename__ = 'users'
    id = db.Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    first_name = Column(String(45))
    last_name = Column(String(45))
    username = Column(String(45), nullable=False)
    password = Column(String(45), nullable=False)
    date_of_birth = Column(DATETIME, default=datetime.datetime.now)
    created = Column(DATETIME, default=datetime.datetime.now)
    updated = Column(DATETIME, default=datetime.datetime.now, onupdate=datetime.datetime.now)
    email = Column(String(45), default="ex@mail.com")

@app.route('/')
def hello_world():
    # return "hello world"
    session = Session()

    test_user = session.query(Users)[0]

    return 'Hello World!' + test_user.first_name

if __name__ == '__main__':
    app.run()


# https://docs.sqlalchemy.org/en/14/dialects/mysql.html#mysql-data-types

# class CategoryEnum(enum.Enum):
#     airplane = 'airplane'
#     rotorcraft = 'rotorcraft'
#     glider = 'glider'
#     poweredPara = 'powered parachute'
#     lighter = 'lighter than air'
#     poweredLift = 'powered lift'
#     weightShift = 'weight shift control'
#
#


# class Aircrafts(db.Model):
#     __tablename__ = 'aircrafts'
#     id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
#     airClass = Column('class', String(45))
#     type = Column(String(45))
#     identification = Column
#
#
# class Logs(db.Model):
#     __tablename__ = 'logs'
#
#
# class Ratings(db.Model):
#     __tablename__ = 'ratings'




