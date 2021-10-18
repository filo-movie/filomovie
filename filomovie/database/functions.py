from filomovie import db, relation_dictionary
from filomovie.database import base_functions

def insert_movie(id, image, title, description, streaming_services):
    base_functions.insert_movie(db, relation_dictionary["Movie"], id, image, title, description, streaming_services)

def search_title(title):
    base_functions.search_title(relation_dictionary["Movie"], title)

