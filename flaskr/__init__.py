from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session

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


if __name__ == '__main__':
    app.run()





