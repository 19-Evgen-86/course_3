from backend.dao.favorites import FavoritesDao
from backend.tools.decorators import handling_exceptions
from backend.tools.secure import decode_token


class FavoritesService:
    def __init__(self, favorites_movies_dao: FavoritesDao):
        self.favorites_movies_dao = favorites_movies_dao

    @handling_exceptions
    def add(self, movie_id, token):
        email = decode_token(token)["email"]
        self.favorites_movies_dao.add(email, movie_id)

    def delete(self,movie_id, token):
        email = decode_token(token)["email"]
        self.favorites_movies_dao.delete(email, movie_id)