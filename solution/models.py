from flask import Flask
from flask_sqlalchemy import SQLAlchemy




app = Flask(__name__)
#For using with Postgres
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:password@localhost/flasksample"

#For using with mysql
#app.config['SQLALCHEMY_DATABASE_URI'] = "mysql://root:@localhost/flaskSample"
db = SQLAlchemy(app)


class Users(db.Model):
    # you can even specify the table name with which you are working.
    #__tablename__ = 'users'
    name = db.Column(db.String(100), primary_key = True, unique=False, nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(250), unique = False, nullable=False)


"""
Stop the program and run this in python
from project import db, create_app, models
db.create_all(app=create_app()) # pass the create_app result so Flask-SQLAlchemy gets the configuration

"""