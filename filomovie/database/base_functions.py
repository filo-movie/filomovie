from sqlalchemy import func
# Function takes the database connection (db), the Movie table/object, the movie id, movie image,
# movie title, movie description, and movie streaming_services.
# Adds the data to the database if it doesn't exist already and returns True.
# If the record already exists, will print to the screen and return False.
def insert_movie(db, Movie, id, image, title, description, streaming_services):
    if Movie.query.filter_by(id=id).all():
        print('\033[92m' + "[*] Movie '" + str(Movie.query.filter_by(id=id).all()[0].title) + "', id=" + str(id) + " already present in the database" + '\033[0m')
        return False
    elif type(id) != int or type(image) != str or type(title) != str or type(description) != str or type(streaming_services) != str:
        print('\033[92m' + "[*] One or more of the input values was of the incorrect type."+ '\033[0m')
        return False
    else:
        db.session.add(Movie(id, image, title, description, streaming_services))
        db.session.commit()
        print('\033[92m' + "[*] The following movie was added: " + "\n\t" + str(Movie.query.filter_by(id=id).all()[0].title) + ", id=" + str(id) + '\033[0m')
        return True


# Searches the title in the database and returns a list of all records that match.
# If no records exist, returns an empty list (will act as False if called in logic).
def search_title(Movie, title):
    movies_found = Movie.query.filter(func.lower(Movie.title).contains(title.lower())).all()
    if movies_found:
        # print('\033[92m' + "[*] Search results for the movie: " + title + " found.\033[0m")
        # for movie in movies_found:
        #     print(f"\tid={movie.id}, \n\timage={movie.image}, \n\ttitle={movie.title}, \n\tdescription={movie.description}, \n\tstreaming_services={movie.streaming_services}" + '\033[0m')
        # print()
        return movies_found
    else:
        return []

def delete_movie(db, Movie, id):
    movies = Movie.query.filter_by(id=id).all()
    if not movies:
        return False
    for movie in movies:
        print(f"Deleting the following movie id: {str(id)}")
        db.session.delete(movie)
        db.session.commit()
    return True

