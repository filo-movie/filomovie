import json
import os

from flask import (
    Flask, Blueprint, flash, redirect, render_template, request, session, url_for
)

from filomovie import backend, app



@app.route('/', methods=('GET', 'POST'))
def index():
    return render_template('index.html')


@app.route('/home', methods=('GET', 'POST'))
def home():
    return render_template('index.html')


'''
 NOTE:  page result will be dynamically generated in the future
        the returned data will be send to backend via post request from the form
'''
@app.route('/search', methods=('GET', 'POST'))
def search():
    # search_result = None
    if request.method == "POST":
        searchedTitle = request.form.get("movie_title")
        search_result = backend.process_search(searchedTitle)

    # this is supposed to the dictionary object to front end
    return render_template('searched_movies.html', search_result=search_result)


@app.route('/json_handler', methods=('GET', 'POST'))
def json_handler():
    if request.method == "POST":
        movieDetails = request.get_json()
        session['movieDetails'] = movieDetails
        # print("\tget request: " + str(movieDetails), flush=True)
        movie_details()
        # return redirect(url_for("movie_details", movieDetails=movieDetails)) #, movieDetails=movieDetails))
    return ('', 204)



@app.route('/movie_details', methods=('GET', 'POST'))
def movie_details():
    curDetail = session['movieDetails']
    movieDetails = backend.process_detail(curDetail)
    return render_template('movie_details.html', movieDetails=movieDetails)


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
