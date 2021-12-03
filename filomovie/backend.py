# from enum import EnumMeta
# from operator import countOf, pos
# import operator
# from os import pardir

# from werkzeug.datastructures import FileMultiDict
# from filomovie import app
from filomovie.database import functions, base_functions
import json

from filomovie import relation_dictionary

# backend processing search
def process_search(searchedMovie):
    movieJsonObj = {}
    # moviesFound is a list containing all movie dictionary object(s)
    movieJsonObj['moviesFound'] = []

    movieObjQuery = base_functions.search_title(relation_dictionary["Movie"], searchedMovie)
    for movie in movieObjQuery:
        curObj = {}
        curObj['movie_id'] = movie.id
        curObj['movie_title'] = movie.title
        curObj['movie_image'] = movie.image
        # NOTE: escaping double quotes cuz they fucked up json
        curObj['movie_desc'] = movie.description.replace('"', '\\"')
        curObj['streaming_services'] = movie.streaming_services.replace('"', '\\"')
        curObj['movie_runtime'] = movie.runtime

        # NOTE: parsing rating decimal to string to fix json decimal error
        curObj['movie_rating'] = str(movie.rating)
        curObj['movie_release_date'] = movie.release_date

        # FIXME: fix after merging with dev
        curObj['movie_genres'] = movie.genres.replace('"', '\\"')

        movieJsonObj['moviesFound'].append(curObj)
    # print("size of result: " + str(len(movieJsonObj['moviesFound'])), flush=True)

    # this is supposed to return a python dictionary
    return movieJsonObj


# sanitize movie details json data
def process_detail(postedJson):
    tempDict = {}
    tempDict['movie_id'] = postedJson['movie_id']
    tempDict['movie_title'] = postedJson['movie_title']
    tempDict['movie_image'] = postedJson['movie_image']
    tempDict['movie_desc'] = postedJson['movie_desc'].replace('"', "\'")

    tempDict['movie_runtime'] = postedJson['movie_runtime']
    tempDict['movie_rating'] = postedJson['movie_rating']
    tempDict['movie_release_date'] = postedJson['movie_release_date']

    tempDict['streaming_services'] = []
    for service in json.loads(postedJson['streaming_services']):
        tempDict['streaming_services'].append(service)

    tempDict['movie_genres'] = []
    for genre in json.loads(postedJson['movie_genres']):
        tempDict['movie_genres'].append(genre)

    return tempDict
