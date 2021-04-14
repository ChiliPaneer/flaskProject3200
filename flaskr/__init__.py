from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session

from sqlalchemy import Table, MetaData, Column, Integer, String, TIMESTAMP, DATETIME
from sqlalchemy import text
from sqlalchemy.schema import FetchedValue

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:P@ssw0rd@localhost/python_test'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = 'FALSE'


@app.route('/')
def hello_world():
    return 'Hello World!'

db = SQLAlchemy(app)

Base = automap_base()

engine = create_engine(
    'mysql+pymysql://root:P@ssw0rd@localhost/python_test',
    echo=True
)

Base.prepare(engine, reflect=True)
user = Base.classes.users
session = Session(engine)
res = session.query(user).first()
print(res.first_name)

print('hello')
print('new feautre on demoBranch')


if __name__ == '__main__':
    app.run()


# https://docs.sqlalchemy.org/en/14/dialects/mysql.html#mysql-data-types

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(Integer, primary_key=True)
    first_name = Column(String(45))
    last_name = Column(String(45))
    username = Column(String(45))
    password = Column(String(45))
    date_of_birth = Column(
        DATETIME,
        server_default=text("CURRENT_DATETIME ON UPDATE CURRENT_DATETIME"),
        #server_onupdate=FetchedValue()
    )






