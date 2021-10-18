import unittest
from flask import Flask
import os
from filomovie import database
from filomovie.database import functions

def create_app():
    print("[*] Creating App....", flush=True)
    app = Flask(__name__,
                static_folder='static',
                template_folder='static/templates')

    app.config.from_mapping(
        SECRET_KEY=os.environ.get("SECRET_KEY") or 'dev_key',
        SQLALCHEMY_DATABASE_URI=os.environ.get("DATABASE_URL").replace("postgres", "postgresql"),
        SQLALCHEMY_TRACK_MODIFICATIONS=False,
        TESTING=True
    )

    return app

def drop_test_values():
    inserted_record = relation_dictionary["Movie"].query.filter_by(id=-1).all()
    if inserted_record:
        for record in inserted_record:
            db.session.delete(record)
    second_inserted_record = relation_dictionary["Movie"].query.filter_by(id=-2).all()
    if second_inserted_record:
        for record in second_inserted_record:
            db.session.delete(record)
    db.session.commit()

app = create_app()
db, relation_dictionary = database.create_database(app)

class TestInsert(unittest.TestCase):
    # Test that a set of values can be inserted and queried correctly. Then deletes the value.
    def test_insert(self):
        drop_test_values()
        self.assertTrue(functions.insert_movie(db, relation_dictionary["Movie"], -1, "Some image", "Shrek",
                                               "A movie about an ogre and a donkey.",
                                               "Available on some streaming services"))
        insertedValue = relation_dictionary["Movie"].query.filter_by(id=-1).all()
        self.assertEqual(insertedValue[0].id, -1)
        self.assertEqual(insertedValue[0].image, "Some image")
        self.assertEqual(insertedValue[0].title, "Shrek")
        self.assertEqual(insertedValue[0].description, "A movie about an ogre and a donkey.")
        self.assertEqual(insertedValue[0].streaming_services, "Available on some streaming services")
        drop_test_values()

    # Test that the function returns False if a movie with the same id already exists. Then deletes the value.
    def test_double_insert(self):
        drop_test_values()
        self.assertTrue(functions.insert_movie(db, relation_dictionary["Movie"], -1, "Some image", "Shrek",
                                               "A movie about an ogre and a donkey.",
                                               "Available on some streaming services"))
        self.assertFalse(functions.insert_movie(db, relation_dictionary["Movie"], -1, "Some image", "Shrek",
                                               "A movie about an ogre and a donkey.",
                                               "Available on some streaming services"))
        drop_test_values()

    # Test that the function returns False if one or more input values are of the incorrect type.
    def test_input_types(self):
        self.assertFalse(functions.insert_movie(db, relation_dictionary["Movie"], -1, -1, -1, -1, -1))

class TestQuery(unittest.TestCase):
    # Tests that an empty list is returned if no movie title matches the search, an empty list evaluates to false.
    def test_noMovie(self):
        self.assertFalse(functions.search_title(relation_dictionary["Movie"], "QWERTY"))

    # Tests that all relevant movies are returned when searched by title.
    def test_return_movies(self):
        drop_test_values()
        functions.insert_movie(db, relation_dictionary["Movie"], -1, "Some image", "Shrek",
                               "A movie about an ogre and a donkey.",
                               "Available on some streaming services")
        functions.insert_movie(db, relation_dictionary["Movie"], -2, "Some image", "Shrek",
                               "A movie about an ogre and a donkey.",
                               "Available on some streaming services")
        records = functions.search_title(relation_dictionary["Movie"], "Shrek")
        self.assertEqual(records[0].id, -1)
        self.assertEqual(records[0].image, "Some image")
        self.assertEqual(records[0].title, "Shrek")
        self.assertEqual(records[0].description, "A movie about an ogre and a donkey.")
        self.assertEqual(records[0].streaming_services, "Available on some streaming services")
        self.assertEqual(records[1].id, -2)
        self.assertEqual(records[1].image, "Some image")
        self.assertEqual(records[1].title, "Shrek")
        self.assertEqual(records[1].description, "A movie about an ogre and a donkey.")
        self.assertEqual(records[1].streaming_services, "Available on some streaming services")
        drop_test_values()


if __name__ == '__main__':
    unittest.main()




