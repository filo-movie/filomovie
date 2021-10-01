from flask_sqlalchemy import SQLAlchemy

def create_database(app):
    db = SQLAlchemy(app)

    class Integer(db.Model):
        __tablename__ = "testTable"
        integer = db.Column(db.Integer)

        def __init__(self, integer):
            self.integer = integer

    return db


