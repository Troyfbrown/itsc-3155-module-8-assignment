# TODO: Feature 3
from flask.testing import FlaskClient
from src.repositories.movie_repository import movie_repository_singleton

def test_search_movies_page(test_app: FlaskClient):
    movie_repository_singleton.create_movie('Super', 'Man', 2)
    response = test_app.get('/movies/search?title=Super')
    response_data = response.data
    assert b'The rating of Super is 2' in response_data
    response = test_app.get('/movies/search?title=Baby Driver')
    response_data = response.data
    assert b'Movie not found' in response_data