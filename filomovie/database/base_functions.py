from sqlalchemy import func
# Function takes the database connection (db), the Movie table/object, the movie id, movie image,
# movie title, movie description, and movie streaming_services.
# Adds the data to the database if it doesn't exist already and returns True.
# If the record already exists, will print to the screen and return False.
def insert_movie(db, Movie, id, image, title, description, streaming_services):
    if Movie.query.filter_by(id=id).all():
        print("Movie '" + str(Movie.query.filter_by(id=id).all()[0].title) + "', id=" + str(id) + " already present in the database")
        return False
    elif type(id) != int or type(image) != str or type(title) != str or type(description) != str or type(streaming_services) != str:
        print("One or more of the input values was of the incorrect type.")
        return False
    else:
        db.session.add(Movie(id, image, title, description, streaming_services))
        db.session.commit()
        print("The following movie was added: " + str(Movie.query.filter_by(id=id).all()[0].title) + ", id=" + str(id))
        return True

# Searches the title in the database and returns a list of all records that match.
# If no records exist, returns an empty list (will act as False if called in logic).
def search_title(Movie, title):
    movies_found = Movie.query.filter(func.lower(Movie.title).contains(title.lower())).all()
    if movies_found:
        print("Search results for the movie: " + title)
        for movie in movies_found:
            print(f"id={movie.id}, image={movie.image}, title={movie.title}, description={movie.description}, streaming_services={movie.streaming_services}")
        print()
        return movies_found
    else:
        return []

