'''
ADRIAN: Update the route methods to accoutn for posting and passing in
        parameters into imaginary dao methods (a lot of code will be stolen from DAO/<file>.py
'''

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Logs, Users, Aircrafts, CategoryEnum, CertificateEnum, Ratings
from flask import Flask, render_template
from flaskr.models import db, Logs, Users, Aircrafts, CategoryEnum, CertificateEnum, Ratings
import DAO.users as userDAO
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
    users = userDAO.findAll_users()
    return render_template('list.html', data=users)






# LISTING
@app.route('/', methods = ['POST','GET'])
def hello_world():
    return render_template('landing.html')

@app.route('/list/user', methods = ['POST','GET'])
def users_list():
    #data = #userDAO.findAllUsers()
    return render_template('list.html', string = 'user', data = [[0,1],[0,1]])

@app.route('/list/aircraft', methods = ['POST','GET'])
def aircrafts_list():
    return render_template('list.html', string = 'aircraft',data = [[0,1],[0,1]])

@app.route('/list/log', methods = ['POST','GET'])
def logs_list():
    return render_template('list.html', string = 'log', data = [[0,1],[0,1]])


# UPDATING
@app.route('/create/user/<id>', methods=['POST','GET'])
def update_user(id):
    # if post:
    #     userDAO.creatUser(requests.form['key'],...)
    if not id:
        return render_template('user_edit.html')
    elif id:
        #get all the information about the id#
        return render_template('user_edit.html', id = "4")


@app.route('/create/aircraft/<id>', methods=['POST','GET'])
def update_aircraft(id):
    if not id:
        return render_template('aircraft_edit.html')
    elif id:
        #get all the information about the id#
        return render_template('aircraft_edit.html', id = "2")

@app.route('/create/log/<id>', methods=['POST','GET'])
def update_log(id):
    if not id:
        return render_template('log_edit.html')
    elif id:
        #get all the information about the id#
        return render_template('log_edit.html', id = "3")



# CREATING

@app.route('/create/log', methods=['POST','GET'])
def create_log():
    return render_template('log_edit.html')


@app.route('/create/aircraft', methods=['POST','GET'])
def create_aircraft():
    return render_template('aircraft_edit.html')

@app.route('/create/user', methods=['POST','GET'])
def create_user():
    return render_template('user_edit.html')




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
