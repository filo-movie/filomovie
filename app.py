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
    return render_template('indextest.html')


@app.route('/home', methods=('GET', 'POST'))
def home():
    return render_template('indextest.html')


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
    return render_template('indextest.html')


@app.route('/shrek1', methods=('GET', 'POST'))
def shrek1():
    return render_template('shrek_1.html')

@app.route('/shrek2', methods=('GET', 'POST'))
def shrek2():
    return render_template('shrek_2.html')

@app.route('/shrek3', methods=('GET', 'POST'))
def shrek3():
    return render_template('shrek_3.html')


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
