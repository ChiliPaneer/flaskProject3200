# TODO REFACTOR AS DISCUSSED CHRISTINA
from flask import request, render_template, make_response
from flaskr.models import db, Logs, Users, Aircrafts,  Ratings
from flaskr.__init__ import db
from datetime import datetime as dt


# attribution: Todd Birchard @hackersandslackers.com

def createAircraft(airClass, type, identification, category):
    new_aircrafts = Aircrafts(
        # TODO a_class rep. class with is a keyword in python, possible conflict?
        airClass=airClass,
        type=type,
        identification=identification,
        category=category,
        created=dt.now(),
        updated=dt.now()
    )
    db.session.add(new_aircrafts)  # Adds new User record to database
    db.session.commit()  # Commits all changes

# finds all aircrafts in the table
def findAllAircrafts():
    aircrafts = db.session.query(Aircrafts).all()
    return aircrafts

def findAircraftById(id):
    aircraft = db.session.query(Aircrafts).get(id)
    return aircraft


def updateAircraft(id, airClass, type, identification, category):
    # which aircraft is being updated
    aircraft = db.session.query(Aircrafts).get(id)
    # get updated fields
    if airClass:
        aircraft.airClass = airClass
    if type:
        aircraft.type = type
    if identification:
        aircraft.identification = identification
    if category:
        aircraft.category = category
    aircraft.updated = dt.now()
    db.session.commit()


def deleteAircraft(id):
    obj = db.session.query(Aircrafts).filter(Aircrafts.id == id).first()
    db.session.delete(obj)
    db.session.commit()
