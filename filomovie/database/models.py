from flask_sqlalchemy import SQLAlchemy

def create_database(app):
    db = SQLAlchemy(app)

    class Integer(db.Model):
        __tablename__ = "testTable"
        integer = db.Column(db.Integer, primary_key=True)

        def __init__(self, integer):
            self.integer = integer

    return db

