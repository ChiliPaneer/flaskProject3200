from flask import request, render_template, make_response
from datetime import datetime as dt
from flask import current_app as app
from flaskr.models.users import Users
from flaskr.models import users
from flaskr import db


# attribution: Todd Birchard @hackersandslackers.com

@app.route('/users', methods=['GET', 'POST'])
def create_users():

    render_template('user_edit.html')
    """Create a user via query string parameters."""
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    username = request.form['username']
    password = request.form['password']
    date_of_birth = request.form['date_of_birth']
    email = request.form['email']

    if first_name and last_name and username and password and date_of_birth and email:
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

    return 1


@app.route('/users', methods=['GET', 'POST'])
def findAll_users():
    userlist = db.session.query(users).all()
    return render_template('list.html', userlist)


@app.route('/users/<id>' , methods=['GET', 'POST'])
def findByID_users(id):
    user = db.session.query(users).get(id)
    return 1


@app.route('/users/<id>' , methods=['GET', 'POST'])
def update_users(id):
    # which user is being updated
    user = db.session.query(users).get(id)
    render_template('list.html', user)

    # get updated fields
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    username = request.form['username']
    password = request.form['password']
    date_of_birth = request.form['date_of_birth']
    email = request.form['email']

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
    db.session.commit()


@app.route('/users/<id>', methods=['GET', 'POST'])
def delete_users(id):
    # id = int(request.form['id'])
    obj = db.session.query(users).filter(users.id == id).first()
    db.session.delete(obj)
    db.session.commit()
