"""Flask configuration variables."""
from os import environ, path
# TODO had to pip install python-dotenv for this, gave errors when running server though
from dotenv import load_dotenv

basedir = path.abspath(path.dirname(__file__))
load_dotenv(path.join(basedir, '.env'))


class Config:
    """Set Flask configuration from .env file."""

    # General Config
    SECRET_KEY = environ.get('SECRET_KEY')
    FLASK_APP = environ.get('FLASK_APP')
    FLASK_ENV = environ.get('FLASK_ENV')

    # Database
    SQLALCHEMY_DATABASE_URI = environ.get('mysql+pymysql://root:C9Sneaky@localhost/python_test')
    SQLALCHEMY_ECHO = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False