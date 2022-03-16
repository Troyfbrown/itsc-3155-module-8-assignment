# TODO: Feature 3
from flask.testing import FlaskClient
from src.repositories.movie_repository import MovieRepository

def test_get_movie_by_title_movies():
    mainvariable = MovieRepository()
   
    # add movies to list
    mainvariable.create_movie("Pire", "Phil", 2)
    mainvariable.create_movie("Mire", "Mhil", 1)


    # making sure the variables work
    assert mainvariable.get_movie_by_title("Pire").director == "Phil"
    assert mainvariable.get_movie_by_title("Mire").title == "Mire"


    # new movies
    movie1 = mainvariable.get_movie_by_title("Phire")
    movie2 = mainvariable.get_movie_by_title("no movie")


    # test
    assert movie1 is not None
    assert movie2 is None
