import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

'''
NOTE: database setup boilerplate code. modify to your needs 
''' 

# create db object
# db = SQLAlchemy()
# migrate = Migrate()

# initialize app and database connection
def create_app():
    app = Flask(__name__,
                static_folder= 'static',
                template_folder='static/templates')

    # TODO: setup database connection here?
    # app.config.from_mapping(
    #     SECRET_KEY = os.environ.get('SECRET_KEY') or 'dev_key',
    #     SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
    #         'sqlite:///' + os.path.join(app.instance_path, 'task_list.sqlite'),
    #     SQLALCHEMY_TRACK_MODIFICATIONS = False
    # )

    # db.init_app(app)
    # migrate.init_app(app, db)
    return app


app = create_app()


