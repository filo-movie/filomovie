from enum import EnumMeta
import sys
import os

from flask import (
    Flask, Blueprint, flash, redirect, render_template, request, url_for
)
from filomovie import app
import filomovie
from filomovie.database import functions
# import filomovie.database.functions



# backend processing search
def process_search(searchedMovie):
    #NOTE: #35 test fill up dummy data for search
    functions.filling_up_database()

    print('\033[95m' + "[*] You searched: " + searchedMovie + '\033[0m' + "\n", flush=True)

    search_movie_query = functions.search_title(searchedMovie) #[0]

    # found movie
    if len(search_movie_query) != 0:
        print('\033[95m' + "[*] Found movie " + searchedMovie + ". \n[*] search_title() returns: " + str(search_movie_query[0]) + '\033[0m' + "\n", flush=True)

    # not found
    else:
        print('\033[95m' + "[*] " + searchedMovie + " not found. " + "\n[*] search_title() returned:" + str(search_movie_query) + '\033[0m' + "\n", flush=True)

    # deleting dummy data
    functions.deleting_dummy_data()

    return searchedMovie
