from operator import truediv
import os
from flask import Flask
from flask_migrate import Migrate
from filomovie.database import test_conn, create_database


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
        TESTING=True
    )
    
    return app


app = create_app()
db, schema_dictionary = create_database(app)
if app.config.get("TESTING"):
    test_conn(db, schema_dictionary["Integer"])
migrate = Migrate(app, db)