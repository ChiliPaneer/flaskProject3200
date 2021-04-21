#TODO REFACTOR AS DISCUSSED CHRISTINA
'''
from flask import request, render_template, make_response
from datetime import datetime as dt
from flask import current_app as app
from flaskr.models import db, aircrafts
# attribution: Todd Birchard @hackersandslackers.com
@app.route('/aircrafts', methods=['GET', 'POST'])
def create_aircrafts():
    """Create a route via query string parameters."""
    a_class = request.form['a_class']
    a_type = request.form['type']
    identification = request.form['identification']
    category = request.form['category']
    if a_class and a_type and identification and category:
        new_aircrafts = aircrafts(
            # TODO a_class rep. class with is a keyword in python, possible conflict?
            a_class=a_class,
            type=a_type,
            identification=identification,
            category=category,
            created=dt.now(),
            updated=dt.now()
        )
        db.session.add(new_aircrafts)  # Adds new User record to database
        db.session.commit()  # Commits all changes
    return render_template('list.html')
@app.route('/aircrafts', methods=['GET', 'POST'])
def findAll_aircrafts():
    aircrafts = db.session.query(aircrafts).all()
    return render_template('list.html', aircrafts)
@app.route('/aircrafts'/ 'id', methods=['GET', 'POST'])
def findByID_aircrafts(id):
    aircrafts = db.session.query(aircrafts).get(id)
    return render_template('list.html', aircrafts)
@app.route('/aircrafts'/ 'id', methods=['GET', 'POST'])
def update_aircrafts(id):
    # which aircraft is being updated
    aircraft = db.session.query(aircrafts).get(id)
    # get updated fields
    a_class = request.form['a_class']
    a_type = request.form['type']
    identification = request.form['identification']
    category = request.form['category']
    # check if fields are filled and replace if filled
    if a_class:
        aircraft.a_class = a_class
    if a_type:
        aircraft.type = a_type
    if identification:
        aircraft.identification = identification
    if category:
        aircraft.category = category
    db.session.commit()
@app.route('/aircrafts' / 'id', methods=['GET', 'POST'])
def delete_aircrafts(id):
    # id = int(request.form['id'])
    obj = db.session.query(aircrafts).filter(aircrafts.id == id).first()
    db.session.delete(obj)
    db.session.commit()
'''