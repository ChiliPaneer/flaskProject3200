'''
ADRIAN: implement rest of DAOs

'''

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Logs, Users, Aircrafts, CategoryEnum, CertificateEnum, Ratings
from flask import Flask, render_template, request, redirect
from flaskr.models import db, Logs, Users, Aircrafts, CategoryEnum, CertificateEnum, Ratings
import DAO.users as userDAO
import DAO.logs as logDAO
import DAO.ratings as ratingDAO
import DAO.users as userDAO
import DAO.aircrafts as aircraftDAO
from datetime import datetime

# Configuring SQL Alchemy, don't touch
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:P@ssw0rd@localhost/python_test'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = 'FALSE'

engine = create_engine(
    'mysql+pymysql://root:P@ssw0rd@localhost/python_test',
    echo=True
)
Session = sessionmaker(bind=engine)
db.init_app(app)


# Web pages routing


# TESTING
@app.route('/users/list', methods=['GET', 'POST'])
def findAll_users():
    users = users_dao.findAll_users()
    return render_template('list.html', data=users)






# LISTING
@app.route('/', methods=['POST', 'GET'])
def hello_world():
    return render_template('landing.html')


@app.route('/list/user', methods=['POST', 'GET'])
def users_list():
    d = list(userDAO.findAllUsers())
    lst = [list(vars(d[0]).keys())[1:]]
    for i in d:
        lst.append(list(vars(i).values())[1:])
    print(lst)
    return render_template('list.html', string='user', data=lst)


@app.route('/list/aircraft', methods=['POST', 'GET'])
def aircrafts_list():
    d = list(aircraftDAO.findAllAircrafts())
    lst = [list(vars(d[0]).keys())[1:]]
    for i in d:
        lst.append(list(vars(i).values())[1:])
    print(lst)
    return render_template('list.html', string='aircraft', data=lst)


@app.route('/list/log', methods=['POST', 'GET'])
def logs_list():
    d = list(logDAO.findAllLogs())
    lst = [list(vars(d[0]).keys())[1:]]
    for i in d:
        lst.append(list(vars(i).values())[1:])
    return render_template('list.html', string = 'log', data = lst)

@app.route('/list/rating', methods = ["POST",'GET'])
def ratings_list():
    d = list(ratingDAO.findAllRatings())
    lst = [list(vars(d[0]).keys())[1:]]
    for i in d:
        lst.append(list(vars(i).values())[1:])
    return render_template('list.html', string = 'rating', data = lst)


# UPDATING
@app.route('/create/rating/<id>', methods = ['POST','GET'])
def update_rating(id):
    if request.method == "POST":
        certificate = request.form.get('certificate')
        category = request.form.get('category')
        r_class = request.form.get('r_class')
        type = request.form.get('type')
        instrument = request.form.get('instrument')
        user_id = request.form.get('user_id')
        ratingDAO.updateRating(id, certificate, category, r_class, type, instrument, user_id)
        print(id, certificate, category, r_class, type, instrument, user_id)
        print("update")
        return redirect('/') #replace
    else:
        r = ratingDAO.findRatingById(id)
        certificate = r.certificate
        category = r.category
        r_class = r.airClass
        type = r.type
        instrument = r.instrument
        user_id = r.user_id
        return render_template('ratings_edit.html', id = id, certificate = certificate, category = category, r_class = r_class,
                              type = type, instrument = instrument, user_id = user_id)
        #return render_template('ratings_edit.html', id = id)


@app.route('/create/user/<id>', methods=['POST','GET'])
def update_user(id):
    if request.method == "POST":
        first_name = request.form.get('first_name')
        last_name = request.form.get('last_name')
        username = request.form.get('username')
        password = request.form.get('password')
        date_of_birth = request.form.get('date_of_birth')
        date_of_birth = datetime.strptime(date_of_birth, "%Y-%m-%d")
        email = request.form.get('email')
        userDAO.updateUser(id, first_name, last_name, username, password, date_of_birth, email)
        print(date_of_birth)
        print(id, first_name, last_name, username, password, date_of_birth, email)
        print("update")
        return redirect('/')
    else:
        u = userDAO.findUserById(id)
        first_name = u.first_name
        last_name = u.last_name
        username = u.username
        password = u.password
        date_of_birth = u.date_of_birth
        email = u.email
        return render_template('user_edit.html', id = id, first_name=first_name, last_name=last_name, username=username, password=password, date_of_birth=date_of_birth, email=email)
        #return render_template('user_edit.html', id=id)



@app.route('/create/aircraft/<id>', methods=['POST','GET'])
def update_aircraft(id):
    if request.method == "POST":

        a_class = request.form.get('a_class')
        type = request.form.get('type')
        identification = request.form.get('identification')
        category = request.form.get('category')
        aircraftDAO.updateAircraft(id, a_class, type, identification, category)
        print(id, a_class, type, identification, category)
        print("update")
        return redirect('/')
    else:
        ac = aircraftDAO.findAircraftById(id)

        a_class = ac.airClass
        a_type = ac.type
        identification = ac.identification
        category = ac.category
        return render_template('aircraft_edit.html', id = id, a_class = a_class, type = a_type, identification = identification, category = category)
        #return render_template('aircraft_edit.html', id = id)

@app.route('/create/log/<id>', methods=['POST','GET'])
def update_log(id):
    if request.method == "POST":
        sic_time = request.form.get('sic_time')
        total_time = request.form.get('total_time')
        pic_time = request.form.get('pic_time')
        night_time = request.form.get('night_time')
        day_time = request.form.get('day_time')
        xc_time = request.form.get('xc_time')
        dual_received = request.form.get('dual_received')
        dual_given = request.form.get('dual_given')
        actual_instrument = request.form.get('actual_instrument')
        simulated_instrument = request.form.get('simulated_instrument')
        departure = request.form.get('departure')
        destination = request.form.get('destination')
        via = request.form.get('via')
        day_landings = request.form.get('day_landings')
        night_landings = request.form.get('night_landings')
        num_instrument_approaches = request.form.get('num_instrument_approaches')
        user_id = request.form.get('user_id')
        aircraft_id = request.form.get('aircraft_id')
        remarks = request.form.get('remarks')
        date = request.form.get('date')
        date = datetime.strptime(date,"%Y-%m-%d")
        logDAO.updateLogs(id, sic_time = sic_time, total_time = total_time, pic_time = pic_time, night_time = night_time, day_time = day_time, xc_time = xc_time, dual_received = dual_received,
        dual_given = dual_given, actual_instrument = actual_instrument, simulated_instrument = simulated_instrument, departure = departure, destination = destination, via = via, day_landings = day_landings,
        night_landings = night_landings, num_instrument_approaches = num_instrument_approaches, user_id = user_id, aircraft_id = aircraft_id, remarks = remarks, date = date)
        print("update")
        print(id, sic_time, total_time, pic_time, night_time, day_time, xc_time, dual_received, dual_given,
              actual_instrument, simulated_instrument, departure, destination, via, day_landings, night_landings,
              num_instrument_approaches, user_id, aircraft_id, remarks, date)
        return redirect('/')
    else:
        lg = logDAO.findLogsById(id)
        print(type(lg))
        sic_time = lg.sic_time
        total_time = lg.total_time
        pic_time = lg.pic_time
        night_time = lg.night_time
        day_time = lg.day_time
        xc_time = lg.xc_time
        dual_received = lg.dual_received
        dual_given = lg.dual_given
        actual_instrument = lg.actual_instrument
        simulated_instrument = lg.simulated_instrument
        departure = lg.departure
        destination = lg.destination
        via = lg.via
        day_landings = lg.day_landings
        night_landings = lg.night_landings
        num_instrument_approaches = lg.num_instrument_approaches
        user_id = lg.user_id
        aircraft_id = lg.aircraft_id
        remarks = lg.remarks
        date = lg.date
        return render_template('log_edit.html', id = id, sic_time = sic_time, total_time = total_time,
        pic_time = pic_time, night_time = night_time, day_time = day_time, xc_time = xc_time,
        dual_received = dual_received, dual_given = dual_given, actual_instrument = actual_instrument,
        simulated_instrument = simulated_instrument, departure = departure, destination = destination, via = via,
        day_landings = day_landings,night_landings = night_landings,
        num_instrument_approaches = num_instrument_approaches, remarks = remarks, date = date,
        user_id = user_id, aircraft_id = aircraft_id)
        #return render_template('log_edit.html', id = id)


# CREATING

@app.route('/create/rating', methods = ["POST","GET"])
def create_rating():
    if request.method == "POST":
        certificate = request.form.get('certificate')
        category = request.form.get('category')
        r_class = request.form.get('r_class')
        type = request.form.get('type')
        instrument = request.form.get('instrument')
        user_id = request.form.get('user_id')
        ratingDAO.createRating(certificate, category, r_class, type, instrument, user_id)
        print('create')
        print(certificate, category, r_class, type, instrument, user_id)
        return redirect('/')  # replace
    else:
        return render_template('ratings_edit.html')


@app.route('/create/log', methods=['POST','GET'])
def create_log():
    if request.method == "POST":
        sic_time = request.form.get('sic_time')
        total_time = request.form.get('total_time')
        pic_time = request.form.get('pic_time')
        night_time = request.form.get('night_time')
        day_time = request.form.get('day_time')
        xc_time = request.form.get('xc_time')
        dual_received = request.form.get('dual_received')
        dual_given = request.form.get('dual_given')
        actual_instrument = request.form.get('actual_instrument')
        simulated_instrument = request.form.get('simulated_instrument')
        departure = request.form.get('departure')
        destination = request.form.get('destination')
        via = request.form.get('via')
        day_landings = request.form.get('day_landings')
        night_landings = request.form.get('night_landings')
        num_instrument_approaches = request.form.get('num_instrument_approaches')
        user_id = request.form.get('user_id')
        aircraft_id = request.form.get('aircraft_id')
        date = request.form.get('date')
        date = datetime.strptime(date,"%Y-%m-%d")
        remarks = request.form.get('remarks')
        logDAO.createLog(sic_time = sic_time, total_time = total_time, pic_time = pic_time, night_time = night_time, day_time = day_time, xc_time = xc_time, dual_received = dual_received,
        dual_given = dual_given, actual_instrument = actual_instrument, simulated_instrument = simulated_instrument, departure = departure, destination = destination, via = via, day_landings = day_landings,
        night_landings = night_landings, num_instrument_approaches = num_instrument_approaches, user_id = user_id, aircraft_id = aircraft_id, remarks = remarks, date = date)
        print(sic_time, total_time, pic_time, night_time, day_time, xc_time, dual_received, dual_given,
              actual_instrument, simulated_instrument, departure, destination, via, day_landings, night_landings,
              num_instrument_approaches, user_id, aircraft_id, date, remarks)
        return redirect('/')
    else:
        return render_template('log_edit.html')


@app.route('/create/aircraft', methods=['POST','GET'])
def create_aircraft():
    if request.method == "POST":
        a_class = request.form.get('a_class')
        a_type = request.form.get('type')
        identification = request.form.get('identification')
        category = request.form.get('category')
        aircraftDAO.createAircraft(a_class, a_type, identification, category)
        print(a_class, a_type, identification, category)
        return redirect('/')
    else:
        return render_template('aircraft_edit.html')

@app.route('/create/user', methods=['POST','GET'])
def create_user():
    if request.method == "POST":
        first_name = request.form.get('first_name')
        last_name = request.form.get('last_name')
        username = request.form.get('username')
        password = request.form.get('password')
        date_of_birth = request.form.get('date_of_birth')
        #date_of_birth = datetime.strptime(date_of_birth, "%Y-%m-%d")
        email = request.form.get('email')
        userDAO.createUser(first_name, last_name, username, password, date_of_birth, email)
        print(first_name, last_name, username, password, date_of_birth, email)
        return redirect('/')
    else:
        return render_template('user_edit.html')




#DELETE

@app.route('/delete/rating/<id>', methods = ["POST","GET"])
def delete_rating(id):
    ratingDAO.deleteRating(id)
    print(id)
    return redirect('/')

@app.route('/delete/user/<id>', methods = ["POST","GET"])
def delete_user(id):
    userDAO.deleteUser(id)
    print(id)
    return redirect('/')

@app.route('/delete/log/<id>', methods = ["POST","GET"])
def delete_log(id):
    logDAO.deleteLog(id)
    print(id)
    return redirect('/')

@app.route('/delete/aircraft/<id>', methods = ["POST","GET"])
def delete_aircraft(id):
    aircraftDAO.deleteAircraft(id)
    print(id)
    return redirect('/')

# @app.route('/')
# def hello_world():
#     # return "hello world"
#     session = Session()
#
#     # test_user = session.query(Users)[0]
#
#     test_log = session.query(Logs)
#     ans = ""
#     for l, u in session.query(Logs, Users).filter(Users.id == Logs.user_id).all():
#         ans += str(l.id) + " " + str(l.total_time) + " " + str(u.first_name) + " " + str(u.last_name) + "<br>"
#     return 'Hello World!' + ans


if __name__ == '__main__':
    app.run()

# https://docs.sqlalchemy.org/en/14/dialects/mysql.html#mysql-data-types
