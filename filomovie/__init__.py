from operator import truediv
import os
from flask import Flask
from filomovie.database.models import create_database
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

'''
NOTE: database setup boilerplate code. modify to your needs 
''' 


# initialize app and database connection
def create_app():
    print("[*] Creating App....", flush=True) 
    app = Flask(__name__,
                static_folder= 'static',
                template_folder='static/templates')

    app.config.from_mapping(
        SECRET_KEY = os.environ.get("SECRET_KEY") or 'dev_key',
        SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL").replace("postgres", "postgresql"),
        SQLALCHEMY_TRACK_MODIFICATIONS = False,
        TESTING = True
    )

    return app


app = create_app()
db = SQLAlchemy(app)


class Integer(db.Model):
    __tablename__ = "testTable"
    integer = db.Column(db.Integer, primary_key=True)

    def __init__(self, integer):
        self.integer = integer


migrate = Migrate(app, db)

if app.config.get("TESTING"):
    db.session.add(Integer(1))
    db.session.add(Integer(2))
    db.session.add(Integer(3))
    list_of_integer_objects = Integer.query.all()
    if (list(map(lambda integer_obj: integer_obj.integer, list_of_integer_objects)) == [1, 2, 3]):
        print("[*] ##### Database connection test successful! #####", flush=True) 
    else:
        print("[*] ##### Database connection failed! #####", flush=True) 

