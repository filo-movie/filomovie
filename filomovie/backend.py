from enum import EnumMeta
from operator import countOf, pos
import operator
from os import pardir

from flask import (
    Flask, Blueprint, flash, redirect, render_template, request, url_for
)
from werkzeug.datastructures import FileMultiDict
from filomovie import app
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
        movieJsonObj['moviesFound'].append(curObj)

    print("size of result: " + str(len(movieJsonObj['moviesFound'])), flush=True)

    # this is supposed to return a python dictionary
    return movieJsonObj


def process_detail(postedJson):
    tempDict = {}
    tempDict['movie_id'] = postedJson['movie_id']
    tempDict['movie_title'] = postedJson['movie_title']
    tempDict['movie_image'] = postedJson['movie_image']
    tempDict['movie_desc'] = postedJson['movie_desc'].replace('"', "\'")
    
    tempDict['streaming_services'] = []
    for service in json.loads(postedJson['streaming_services']):
        #print("provider: " + ser, flush=True)
        tempDict['streaming_services'].append(service)

    # print("temp json: " + str(tempDict), flush=True)
    # print("provider json: " + str(tempDict['streaming_services']), flush=True)
    return tempDict
