from enum import EnumMeta
from operator import countOf
from os import pardir

from flask import (
    Flask, Blueprint, flash, redirect, render_template, request, url_for
)
from filomovie import app
from filomovie.database import functions, base_functions
import json

from filomovie import relation_dictionary

# backend processing search
def process_search(searchedMovie):

    functions.filling_up_database()
    # print('\033[95m' + "[*] You searched: " + searchedMovie + '\033[0m' + "\n", flush=True)

    # search_movie_query = functions.search_title(searchedMovie) #[0]
    # found movie
    # if len(search_movie_query) != 0:
    #     print('\033[95m' + "[*] Found movie " + searchedMovie + ". \n[*] search_title() returns: " + str(search_movie_query[0]) + '\033[0m' + "\n", flush=True)
    # # not found
    # else:
    #     print('\033[95m' + "[*] " + searchedMovie + " not found. " + "\n[*] search_title() returned:" + str(search_movie_query) + '\033[0m' + "\n", flush=True)

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

    # deleting dummy data
    functions.deleting_dummy_data()

    # this is supposed to return a python dictionary
    return movieJsonObj
