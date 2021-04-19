import enum
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import sessionmaker, relationship
import datetime

from sqlalchemy import Table, MetaData, Column, Integer, String, TIMESTAMP, DATETIME, Enum, DECIMAL, ForeignKey

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


class CategoryEnum(enum.Enum):
    airplane = 'airplane'
    rotorcraft = 'rotorcraft'
    glider = 'glider'
    poweredPara = 'powered parachute'
    lighter = 'lighter than air'
    poweredLift = 'powered lift'
    weightShift = 'weight shift control'


class CertificateEnum(enum.Enum):
    student = 'student'
    sport = 'sport'
    recreational = 'recreational'
    private = 'private'
    commercial = 'commercial'
    airlineTransport = 'airline transport'


class Aircrafts(db.Model):
    __tablename__ = 'aircrafts'
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    airClass = Column('class', String(45))
    type = Column(String(45))
    identification = Column(String(45))
    category = Column(Enum(CategoryEnum))
    created = Column(DATETIME, default=datetime.datetime.now)
    updated = Column(DATETIME, default=datetime.datetime.now, onupdate=datetime.datetime.now)


class Logs(db.Model):
    __tablename__ = 'logs'
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    sic_time = Column(DECIMAL(10, 1))
    total_time = Column(DECIMAL(10, 1))
    pic_time = Column(DECIMAL(10, 1))
    date = Column(DATETIME)
    night_time = Column(DECIMAL(10, 1))
    day_time = Column(DECIMAL(10, 1))
    xc_time = Column(DECIMAL(10, 1))
    dual_received = Column(DECIMAL(10, 1))
    dual_given = Column(DECIMAL(10, 1))
    actual_instrument = Column(DECIMAL(10, 1))
    # make this instrument in datbase
    simulated_instrument = Column(DECIMAL(10, 1))
    departure = Column(String(4))
    destination = Column(String(4))
    via = Column(String(4))
    day_landings = Column(Integer)
    night_landings = Column(Integer)
    num_instrument_approaches = Column(Integer)
    remarks = Column(String(300))
    user_id = Column(Integer, ForeignKey('users.id', onupdate='cascade'))
    aircraft_id = Column(Integer, ForeignKey('aircrafts.id', ondelete='cascade', onupdate='cascade'))
    created = Column(DATETIME, default=datetime.datetime.now)
    updated = Column(DATETIME, default=datetime.datetime.now, onupdate=datetime.datetime.now)

    logs_to_aircrafts = relationship("Users")  # , back_populates="logs")
    aircraft = relationship("Aircrafts")  # , back_populates="logs")


class Ratings(db.Model):
    __tablename__ = 'ratings'
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    certificate = Column(Enum(CertificateEnum))
    category = Column(Enum(CategoryEnum))
    airClass = Column('class', String(100))
    type = Column(String(200))
    instrument = Column(String(45))
    created = Column(DATETIME, default=datetime.datetime.now)
    updated = Column(DATETIME, default=datetime.datetime.now, onupdate=datetime.datetime.now)

    user_id = Column(Integer, ForeignKey('users.id'))


    # change to ratings_to_users in database
    ratings_to_users = relationship("Users")  # , back_populates="ratings")


@app.route('/')
def hello_world():
    # return "hello world"
    session = Session()

    # test_user = session.query(Users)[0]

    test_log = session.query(Logs)
    ans = ""
    for l, u in session.query(Logs, Users).filter(Users.id == Logs.user_id).all():
        ans += str(l.id) + " " + str(l.total_time) + " " + str(u.first_name) + " " + str(u.last_name) + "<br>"
    return 'Hello World!' + ans


if __name__ == '__main__':
    app.run()

# https://docs.sqlalchemy.org/en/14/dialects/mysql.html#mysql-data-types
