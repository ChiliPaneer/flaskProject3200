
'''
from flask import request, render_template, make_response
from datetime import datetime as dt
from flask import current_app as app
from flaskr.models import db, ratings


# attribution: Todd Birchard @hackersandslackers.com

@app.route('/ratings', methods=['GET', 'POST'])
def create_logs():
    """Create a rating via query string parameters."""
    certificate = request.form['certificate']
    category = request.form['category']
    r_class = request.form['r_class']
    type = request.form['type']
    instrument = request.form['isntrument']
    user_id = request.form['user_id']

    if r_class and type and certificate and category and instrument and user_id:
        new_ratings = ratings(

            # TODO r_class rep. class with is a keyword in python, possible conflict?
            r_class = r_class,
            type=type,
            certificate=certificate,
            category=category,
            instrument = instrument,
            user_id = user_id,
            created=dt.now(),
            updated=dt.now()

        )

        db.session.add(new_ratings)  # Adds new User record to database
        db.session.commit()  # Commits all changes

    return render_template('list.html')


@app.route('/ratings', methods=['GET', 'POST'])
def findAll_ratings():
    aircrafts = db.session.query(ratings).all()
    return render_template('list.html', ratings)


@app.route('/ratings' / 'id', methods=['GET', 'POST'])
def findByID_ratings(id):
    aircrafts = db.session.query(ratings).get(id)
    return render_template('list.html', ratings)


@app.route('/ratings' / 'id', methods=['GET', 'POST'])
def update_ratings(id):
    # which rating is being updated
    rating = db.session.query(ratings).get(id)

    # get updated fields
    r_class = request.form['r_class']
    type = request.form['type']
    instrument = request.form['instrument']
    category = request.form['category']
    certificate = request.form['certificate']
    user_id=request.form['user_id']

    # check if fields are filled and replace if filled
    if r_class:
        rating.r_class = r_class
    if type:
        rating.type = type
    if instrument:
        rating.instrument = instrument
    if category:
        rating.category = category
    if certificate:
        rating.certificate = certificate
    if user_id:
        rating.user_id= user_id
    db.session.commit()


@app.route('/ratings' / 'id', methods=['GET', 'POST'])
def delete_aircrafts(id):
    # id = int(request.form['id'])
    obj = db.session.query(ratings).filter(ratings.id == id).first()
    db.session.delete(obj)
    db.session.commit()
'''