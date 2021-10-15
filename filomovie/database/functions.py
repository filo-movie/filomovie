# Function takes the database connection (db), the Movie table/object, the movie id, movie image,
# movie title, movie description, and movie streaming_services.
# Adds the data to the database if it doesn't exist already and returns True.
# If the record already exists, will print to the screen and return False.
def insert_movie(db, Movie, id, image, title, description, streaming_services):
    if Movie.query.filter_by(id = id).all():
        print("Movie already present in the database")
        return False
    else:
        db.session.add(Movie(id, image, title, description, streaming_services))
        db.session.commit()
        print("The following record was added: " + str(Movie.query.filter_by(id=id).all()))
        return True

# Searches the title in the database and returns a list of all records that match.
# If no records exist, returns an empty list (will act as False if called in logic).
def search_title(Movie, title):
    movies_found = Movie.query.filter_by(title = title).all()
    if movies_found:
        return movies_found
    else:
        return []