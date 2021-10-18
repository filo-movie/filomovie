from filomovie import db, relation_dictionary
from filomovie.database import base_functions

# Inserts a Movie tuple into the database with the given variables. ID MUST BE UNIQUE PER MOVIE.
def insert_movie(id, image, title, description, streaming_services):
    return base_functions.insert_movie(db, relation_dictionary["Movie"], id, image, title, description, streaming_services)

# Returns a list of Movie objects that match the search.
def search_title(title):
    return base_functions.search_title(relation_dictionary["Movie"], title)


# SAMPLE INSERT AND DELETE
'''
insert_movie(-1, "Some image", "Shrek", "A movie about an ogre and a donkey.", "Available on some streaming services")

# Even though the result should only be one value, it is still in a list.
Shrek = search_title("Shrek")[0]

# Example of how to access the values
print(str(Shrek.id) + ", " + Shrek.image + ", " + Shrek.title + ", " + Shrek.description + ", " + Shrek.streaming_services)

# Deletes the value. db.session.delete takes a movie object and removes that tuple from the table.
db.session.delete(Shrek)

# Have to commit changes if you are manually deleting a record, the insert function commits for you.
db.session.commit()
'''

