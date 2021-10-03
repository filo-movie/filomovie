from flask_sqlalchemy import SQLAlchemy

def test_conn(db, Integer):
    db.session.add(Integer(1))
    db.session.add(Integer(2))
    db.session.add(Integer(3))
    list_of_integer_objects = Integer.query.all()
    if list(map(lambda integer_obj: integer_obj.integer, list_of_integer_objects)) == [1, 2, 3]:
        print("[*] ##### Database connection test successful! #####", flush=True)
    else:
        print("[*] ##### Database connection failed! #####", flush=True)


def create_database(app):
    db = SQLAlchemy(app)

    class Integer(db.Model):
        __tablename__ = "testTable"
        integer = db.Column(db.Integer, primary_key=True)

        def __init__(self, integer):
            self.integer = integer

    return db, Integer
