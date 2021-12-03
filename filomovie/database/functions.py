from filomovie import db, relation_dictionary
from filomovie.database import base_functions

# Inserts a Movie tuple into the database with the given variables. ID MUST BE UNIQUE PER MOVIE.
def insert_movie(id, image, title, description, streaming_services, runtime, rating, release_date, genres):
    return base_functions.insert_movie(db, relation_dictionary["Movie"], id, image, title, description, streaming_services, runtime, rating, release_date, genres)

# Returns a list of Movie objects that match the search.
def search_title(title):
    return base_functions.search_title(relation_dictionary["Movie"], title)

def delete_movie(id):
    return base_functions.delete_movie(db, relation_dictionary["Movie"], id)

# NOTE: test filling up dummy data for search
# def filling_up_database():
#     print('\033[92m' + "[*] Creating dummy data \"Shrek\" in Movie database... " + '\033[0m' + "\n", flush=True)
#     insert_movie(-1, "Some image", "Shrek", "A movie about an ogre and a donkey.", "Available on some streaming services")
#     db.session.commit()


# NOTE: delete dummy data from database
# def deleting_dummy_data():
#     print('\033[92m' + "[*] Deleting dummy data \"Shrek\" in Movie database... " + '\033[0m' + "\n", flush=True)
#     Shrek = search_title("Shrek") #[0]
#     if len(Shrek) != 0:
#         foundShrek = Shrek[0]
#         db.session.delete(foundShrek)
#     db.session.commit()


# SAMPLE INSERT AND DELETE. Test filling up database
# def test_filling_up_database():

#     # SAMPLE INSERT AND DELETE
#     print('\033[92m' + "[*] Creating dummy data \"Shrek\" in Movie database... " + '\033[0m', flush=True)

#     insert_movie(-1, "Some image", "Shrek", "A movie about an ogre and a donkey.", "Available on some streaming services")

#     # Even though the result should only be one value, it is still in a list.
#     Shrek = search_title("Shrek")[0]

#     # Example of how to access the values
#     print('\033[92m' + "[*] Found data in database: " + "\n\t" + str(Shrek.id) + ", \n\t" + Shrek.image + ", \n\t" + Shrek.title + ", \n\t" + Shrek.description + ", \n\t" + Shrek.streaming_services + '\033[0m', flush=True)

#     # Deletes the value. db.session.delete takes a movie object and removes that tuple from the table.
#     # db.session.delete(Shrek)

#     # Have to commit changes if you are manually deleting a record, the insert function commits for you.
#     db.session.commit()

