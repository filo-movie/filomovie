import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

'''
NOTE: database setup boilerplate code. modify to your needs 
''' 


# initialize app and database connection
def create_app():
    app = Flask(__name__,
                static_folder= 'static',
                template_folder='static/templates')

    app.config.from_mapping(
        SECRET_KEY = os.environ.get("SECRET_KEY") or 'dev_key',
        SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL'],
        SQLALCHEMY_TRACK_MODIFICATIONS = False,
        TESTING = True
    )

    return app


app = create_app()

db = SQLAlchemy(app)
