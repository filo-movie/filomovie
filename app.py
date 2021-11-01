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
    return render_template('index.html')


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
        # this is supposed to send JSON data to searched_movies.html
        backend.process_search(searchedTitle)
    # user is a JSON object
    user = {"movie_id": "2", "movie_title": "Forrest Gump", "movie_image": "https://image.tmdb.org/t/p/original/saHP97rTPS5eLmrLQEcANmKrsFl.jpg", "movie_desc": "A man with a low IQ has accomplished great things in his life and been present during significant historic events-in each case, far exceeding what anyone imagined he could do. But despite all he has achieved, his one true love eludes him.", "stream_providers": ["fubotV", "Showtime Amazon Channel", "Showtime Roku Premium Channel", "Showtime", "DIRECTV", "Spectrum On Demand"]}
    return render_template('searched_movies.html', user=user)


@app.route('/movie_details', methods=('GET', 'POST'))
def movie_details():
    return render_template('movie_details.html')


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
