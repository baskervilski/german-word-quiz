import os
from dotenv import load_dotenv

basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, '.env'))

FLASK_ENV = 'development'
SECRET_KEY = os.environ.get('SECRET_KEY')

class Config:

    DEBUG = True
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///students.sqlite3'
