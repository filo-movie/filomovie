from flask_sqlalchemy import SQLAlchemy

# Function takes a database connection and the class 'Integer' (as defined in the database set up).
# Prints if the connection is successful or not to the screen.
def test_conn(db, Integer):
    db.session.add(Integer(1))
    db.session.add(Integer(2))
    db.session.add(Integer(3))
    list_of_integer_objects = Integer.query.all()
    if list(map(lambda integer_obj: integer_obj.integer, list_of_integer_objects)) == [1, 2, 3]:
        print("[*] ##### Database connection test successful! #####", flush=True)
    else:
        print("[*] ##### Database connection failed! #####", flush=True)

# Function takes an app and creates the database and relations (tables) that will be used.
# Returns both the database object and the relation classes.
def create_database(app):
    db = SQLAlchemy(app)

    class Integer(db.Model):
        __tablename__ = "testTable"
        integer = db.Column(db.Integer, primary_key=True)

        def __init__(self, integer):
            self.integer = integer

    return db, Integer
