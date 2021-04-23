# TODO REFACTOR AS DISCUSSED CHRISTINA
from flask import request, render_template, make_response
from flaskr.models import db, Logs, Users, Aircrafts,  Ratings
from flaskr.__init__ import db
from datetime import datetime as dt


# attribution: Todd Birchard @hackersandslackers.com

def createRating(certificate, category, airClass, type, instrument, user_id):

    new_ratings = Ratings(
        airClass=airClass,
        type=type,
        certificate=certificate,
        category=category,
        instrument=instrument,
        user_id=user_id,
        created=dt.now(),
        updated=dt.now()
        )
    db.session.add(new_ratings)  # Adds new User record to database
    db.session.commit()  # Commits all changes


def findAllRatings():
    ratings = db.session.query(Ratings).all()
    return ratings


def findRatingById(id):
    rating = db.session.query(Ratings).get(id)
    return rating


def updateRating(id, certificate, category, airClass, type, instrument, user_id):
    # which rating is being updated
    rating = db.session.query(Ratings).get(id)

    # check if fields are filled and replace if filled
    if airClass:
        rating.airClass = airClass
    if type:
        rating.type = type
    if instrument:
        rating.instrument = instrument
    if category:
        rating.category = category
    if certificate:
        rating.certificate = certificate
    if user_id:
        rating.user_id = user_id
    rating.updated = dt.now()
    db.session.commit()


def deleteRating(id):
    obj = db.session.query(Ratings).filter(Ratings.id == id).first()
    db.session.delete(obj)
    db.session.commit()
