# TODO REFACTOR AS DISCUSSED CHRISTINA

from flask import request, render_template, make_response
from flaskr.models import db, Logs, Users, Aircrafts, CategoryEnum, CertificateEnum, Ratings
from flaskr.__init__ import db
from datetime import datetime as dt


# attribution: Todd Birchard @hackersandslackers.com

def createUser(first_name, last_name, username, password, date_of_birth, email):
    render_template('user_edit.html')
    """Create a user via query string parameters."""
    new_user = Users(
        # TODO how to take in dob input? datetime obj? str?
        first_name=first_name,
        last_name=last_name,
        username=username,
        password=password,
        date_of_birth=dt.fromisoformat(date_of_birth),
        created=dt.now(),
        updated=dt.now(),
        email=email
    )
    db.session.add(new_user)  # Adds new User record to database
    db.session.commit()  # Commits all changes


def findUserById(id):
    user = db.session.query(Users).get(id)
    return user


def findAllUsers():
    users = db.session.query(Users).all()
    return users
    # return render_template('list.html', users)


def updateUser(id, first_name, last_name, username, password, date_of_birth, email):
    # which user is being updated
    user = db.session.query(Users).get(id)

    # check if fields are filled and replace if filled
    if first_name:
        user.first_name = first_name
    if last_name:
        user.last_name = last_name
    if username:
        user.username = username
    if password:
        user.password = password
    if date_of_birth:
        user.date_of_birth = date_of_birth
    if email:
        user.email = email
    user.updated = dt.now()
    db.session.commit()


def deleteUser(id):
    obj = db.session.query(Users).filter(Users.id == id).first()
    db.session.delete(obj)
    db.session.commit()
