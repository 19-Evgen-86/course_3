from dao.model.favorite import favorites
from dao.model.user import User


class FavoritesDao:

    def __init__(self, session):
        self.session = session

    def add(self, email, movie_id):
        with self.session.begin():
            user = self.session.query(User).filter(User.email == email).first()
            self.session.execute(favorites.insert().values([user.id, movie_id]))

    def delete(self, email, movie_id):
        with self.session.begin():
            user = self.session.query(User).filter(User.email == email).first()
            for movie in user.favorite_movies:
                if movie.id == movie_id:
                    user.favorite_movies.remove(movie)
