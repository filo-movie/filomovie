from operator import truediv
import os
from flask import Flask
from flask_migrate import Migrate
import filomovie.database


# initialize app and database connection
def create_app():
    print("[*] Creating App....", flush=True) 
    app = Flask(__name__,
                static_folder= 'static',
                template_folder='static/templates')

    app.config.from_mapping(
        SECRET_KEY=os.environ.get("SECRET_KEY") or 'dev_key',
        SQLALCHEMY_DATABASE_URI=os.environ.get("DATABASE_URL").replace("postgres", "postgresql"),
        SQLALCHEMY_TRACK_MODIFICATIONS=False,
    )
    
    return app


app = create_app()
db, relation_dictionary = database.create_database(app)
migrate = Migrate(app, db)