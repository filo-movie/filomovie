# TODO: app initialization code?
import sys

from flask import (
    Flask, Blueprint, flash, redirect, render_template, request, url_for
)

from filomovie import backend

import os

from filomovie import app


@app.route('/', methods=('GET', 'POST'))
def index():
    return render_template('searched_movies.html')


@app.route('/home', methods=('GET', 'POST'))
def home():
    return render_template('searched_movies.html')


'''
 NOTE:  page result will be dynamically generated in the future
        the returned data will be send to backend via post request from the form
'''
@app.route('/search', methods=('GET', 'POST'))
def search():
    if request.method == "POST":
        searchedTitle = request.form.get("movie_title")
        # NOTE: #35 POST to search
        backend.process_search(searchedTitle)
    return render_template('searched_movies.html')


@app.route('/movie_details', methods=('GET', 'POST'))
def movie_details():
    return render_template('movie_details.html')


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
