import json
import os

from flask import (
    Flask, Blueprint, flash, redirect, render_template, request, url_for
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

    # search_result = {"movie_id": "2", "movie_title": "Forrest Gump", "movie_image": "https://image.tmdb.org/t/p/original/saHP97rTPS5eLmrLQEcANmKrsFl.jpg", "movie_desc": "A man with a low IQ has accomplished great things in his life and been present during significant historic events-in each case, far exceeding what anyone imagined he could do. But despite all he has achieved, his one true love eludes him.", "stream_providers": ["fubotV", "Showtime Amazon Channel", "Showtime Roku Premium Channel", "Showtime", "DIRECTV", "Spectrum On Demand"]}
    # search_result = {'movie_id': '65', 'movie_title': '8 Mile', 'movie_image': 'https://image.tmdb.org/t/p/original/7BmQj8qE1FLuLTf7Xjf9sdIHzoa.jpg", "movie_desc": "The setting is Detroit in 1995. The city is divided by 8 Mile, a road that splits the town in half along racial lines. A young white rapper, Jimmy "B-Rabbit" Smith Jr. summons strength within himself to cross over these arbitrary boundaries to fulfill his dream of success in hip hop. With his pal Future and the three one third in place, all he has to do is not choke.', 'stream_providers': ["fubotV", "Showtime Amazon Channel", "Showtime Roku Premium Channel", "Showtime", "DIRECTV", "Spectrum On Demand"]}

    # print(search_result, flush=True)

    # outputText = str(search_result)
    # print(outputText.encode("utf-8"), flush=True)

    # this is supposed to the dictionary object to front end
    return render_template('searched_movies.html', search_result=search_result)



@app.route('/movie_details', methods=('GET', 'POST'))
def movie_details():
    return render_template('movie_details.html')


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
