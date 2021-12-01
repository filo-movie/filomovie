import unittest
from flask import Flask
import os
from filomovie import database
from filomovie.database import base_functions

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
        self.assertTrue(base_functions.insert_movie(db, relation_dictionary["Movie"], -1, "Some image",
                                                    "theNameOfNoOtherMovie", "Some Description",
                                                    "Available on some streaming services", 100, 9.97, "release",
                                                    "Rom-com"))
        insertedValue = relation_dictionary["Movie"].query.filter_by(id=-1).all()
        self.assertEqual(insertedValue[0].id, -1)
        self.assertEqual(insertedValue[0].image, "Some image")
        self.assertEqual(insertedValue[0].title, "theNameOfNoOtherMovie")
        self.assertEqual(insertedValue[0].description, "Some Description")
        self.assertEqual(insertedValue[0].streaming_services, "Available on some streaming services")
        self.assertEqual(insertedValue[0].runtime, 100)
        self.assertEqual(float(insertedValue[0].rating), 9.97)
        self.assertEqual(insertedValue[0].release_date, "release")
        self.assertEqual(insertedValue[0].genres, "Rom-com")
        drop_test_values()

    # Test that the function returns False if a movie with the same id already exists. Then deletes the value.
    def test_double_insert(self):
        drop_test_values()
        self.assertTrue(base_functions.insert_movie(db, relation_dictionary["Movie"], -1, "Some image",
                                                    "theNameOfNoOtherMovie", "Some Description",
                                                    "Available on some streaming services", 100, 9.97, "release",
                                                    "Rom-com"))
        self.assertFalse(base_functions.insert_movie(db, relation_dictionary["Movie"], -1, "Some image",
                                                    "theNameOfNoOtherMovie", "Some Description",
                                                    "Available on some streaming services", 100, 9.97, "release",
                                                    "Rom-com"))
        drop_test_values()

    # Test that the function returns False if one or more input values are of the incorrect type.
    def test_input_types(self):
        self.assertFalse(base_functions.insert_movie(db, relation_dictionary["Movie"], -1, -1, -1, -1, -1, -1, -1, -1, -1))

# Requires insert_movie to be working.
class TestQuery(unittest.TestCase):
    # Tests that an empty list is returned if no movie title matches the search, an empty list evaluates to false.
    def test_noMovie(self):
        self.assertFalse(base_functions.search_title(relation_dictionary["Movie"], "QWERTY"))

    def test_ifTitleContainsString(self):
        drop_test_values()
        base_functions.insert_movie(db, relation_dictionary["Movie"], -1, "Some image",
                                    "theNameOfNoOtherMovie", "Some Description",
                                    "Available on some streaming services", 100, 9.97, "release", "Rom-com")
        base_functions.insert_movie(db, relation_dictionary["Movie"], -2, "Some image2",
                                    "theNameOfNoOtherFilm2", "Some Description2",
                                    "Available on some streaming services2", 100, 9.97, "release", "Rom-com")
        records = base_functions.search_title(relation_dictionary["Movie"], "theNameOfNoOther")
        self.assertEqual(records[0].id, -1)
        self.assertEqual(records[0].image, "Some image")
        self.assertEqual(records[0].title, "theNameOfNoOtherMovie")
        self.assertEqual(records[0].description, "Some Description")
        self.assertEqual(records[0].streaming_services, "Available on some streaming services")
        self.assertEqual(records[1].id, -2)
        self.assertEqual(records[1].image, "Some image2")
        self.assertEqual(records[1].title, "theNameOfNoOtherFilm2")
        self.assertEqual(records[1].description, "Some Description2")
        self.assertEqual(records[1].streaming_services, "Available on some streaming services2")
        drop_test_values()

    def test_caseInsensitive(self):
        drop_test_values()
        base_functions.insert_movie(db, relation_dictionary["Movie"], -1, "Some image",
                                    "theNameOfNoOtherMovie", "Some Description",
                                    "Available on some streaming services", 100, 9.97, "release", "Rom-com")
        records = base_functions.search_title(relation_dictionary["Movie"], "thenAmeofNoOthErMovie")
        self.assertEqual(records[0].id, -1)
        self.assertEqual(records[0].image, "Some image")
        self.assertEqual(records[0].title, "theNameOfNoOtherMovie")
        self.assertEqual(records[0].description, "Some Description")
        self.assertEqual(records[0].streaming_services, "Available on some streaming services")
        self.assertEqual(records[0].runtime, 100)
        self.assertEqual(float(records[0].rating), 9.97)
        self.assertEqual(records[0].release_date, "release")
        self.assertEqual(records[0].genres, "Rom-com")
        drop_test_values()


# Requires insert_movie to be working
class TestDelete(unittest.TestCase):
    # Tests that delete function does not do anything if there is not a value to delete.
    def test_delete_nonexistent(self):
        drop_test_values()
        self.assertFalse(base_functions.delete_movie(db, relation_dictionary["Movie"], -1))
        drop_test_values()

    # Tests that the delete function deletes the record if it exists.
    def test_delete_record(self):
        drop_test_values()
        base_functions.insert_movie(db, relation_dictionary["Movie"], -1, "Some image", "Shrek",
                                    "A movie about an ogre and a donkey.",
                                    "Available on some streaming services", 100, 9.97, "release", "Rom-com")
        self.assertTrue(base_functions.delete_movie(db, relation_dictionary["Movie"], -1))
        self.assertFalse(relation_dictionary["Movie"].query.filter_by(id=-1).all())
        drop_test_values()

class TestGetRandomMovie(unittest.TestCase):
    # Tests that the random function returns a list with one object in it.
    def test_get_random_movie_returns_one(self):
        random_movie = base_functions.get_random_movie(relation_dictionary["Movie"])
        self.assertEqual(len(random_movie), 1)

if __name__ == '__main__':
    unittest.main()




