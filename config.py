# import the os module
import os

# creation of base directory for application
basedir = os.path.abspath(os.path.dirname(__file__))

# Windows = Documents/chicodes_sept2020/week_5/in_class
# Mac & Linus = Documents/chicodes_sept2020/week_5/in_class

# Config classs
# Configure the database (when we have one) AND configure the
# secret key for the encryption of our submitted forms
class Config():
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you will never guess this...'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///' + os.path.join(basedir, 'app.db')
    # Uri is universal relation something
    # want sqlalchemy to set up or connect to db here called app.db, in root directory
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    # stops module from notifying us everytime database is updated