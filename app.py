import os

from flask import (
    redirect, render_template, request, session, url_for
)

from filomovie import backend, app
from filomovie.database.base_functions import search_title



@app.route('/', methods=('GET', 'POST'))
def index():
    return render_template('index.html')


@app.route('/home', methods=('GET', 'POST'))
def home():
    return render_template('index.html')


@app.errorhandler(Exception)
def all_exception_handler(error):
    print("Error handler: " + str(error))
    return redirect(url_for("home")) 


'''
NOTE: page result will be dynamically generated in the future
      the returned data will be send to backend via post request from the form
'''
@app.route('/search', methods=('GET', 'POST'))
def search():
    if request.method == "POST":
        searchedTitle = request.form.get("movie_title")
        global search_result
        search_result = backend.process_search(searchedTitle)
        # this is supposed to the dictionary object to front end
        return render_template('searched_movies.html', search_result=search_result)
    else:
        return redirect(url_for("home")) 

# json handler to handle json data after clicking on poster
@app.route('/json_handler', methods=('GET', 'POST'))
def json_handler():
    if request.method == "POST":
        movieDetails = request.get_json()
        # storing session
        session['movieDetails'] = movieDetails
        # print("\tget request: " + str(movieDetails), flush=True)
        movie_details()
    return ('', 204)


# display movie_details page with session data
@app.route('/movie_details', methods=('GET', 'POST'))
def movie_details():
    curDetail = session['movieDetails']
    movieDetails = backend.process_detail(curDetail)

    # FIXME: clearing session data in case accessing the same url results in same webpage
    # session.pop('movieDetails')
    return render_template('movie_details.html', movieDetails=movieDetails)


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
