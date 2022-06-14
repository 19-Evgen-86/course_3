from sqlalchemy import desc

from config import PAGE_SIZE
from dao.model.movies import Movie


class MovieDao:
    """
     Класс для взаимодействия c таблицей фильмов в БД
     """

    def __init__(self, session):
        self.session = session

    def get_all_movies(self, sortrig: bool = False, page: int = 0):
        result = self.session.query(Movie)
        if page > 0:
            result = result.limit(PAGE_SIZE).offset(page * PAGE_SIZE)
        if sortrig:
            result = result.order_by(desc(Movie.year))
        return result.all()

    def get_one_movie(self, mid):
        return self.session.query(Movie).get(mid)

    def get_movie_filter(self, filter: dict = None, sortrig: bool = False, page: int = 0):
        result = self.session.query(Movie).filter_by(**filter)
        if page > 0:
            result = result.limit(PAGE_SIZE).offset(page * PAGE_SIZE)
        if sortrig:
            result = result.order_by(desc(Movie.year))
        return result.all()

    def create(self, data):
        with self.session.begin():
            self.session.add(data)

    def update(self, data, mid):
        with self.session.begin():
            self.session.query(Movie).filter(Movie.id == mid).update(data)

    def delete(self, mid):
        with self.session.begin():
            self.session.query(Movie).filter(Movie.id == mid).delete()
