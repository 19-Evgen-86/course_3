from dao.model.movies import Movie
from dao.movie import MovieDao
from schemas.base import MovieSchema
from tools.decorators import handling_exceptions


class MovieService:

    def __init__(self, movie_dao: MovieDao):
        self.movie_dao = movie_dao

    @handling_exceptions
    def get_movie_one(self, mid):
        result = self.movie_dao.get_one_movie(mid)
        if result is None:
            return {"message": f"Movie with ID: '{mid}' not found"}, 404
        else:
            return MovieSchema().dump(result), 200

    @handling_exceptions
    def get_movie_all(self, params: dict):
        sorting: bool = False
        page: int = 0
        filters = {}
        if "status" in params:
            # сортировка (сначала новые)
            sorting = True
        if 'page' in params:
            # пагинация
            page = params["page"]
        if 'director_id' in params:
            filters['director_id'] = params['director_id']
        if 'genre_id' in params:
            filters['genre_id'] = params['genre_id']
        if filters:
            result = self.movie_dao.get_movie_filter(filters, sorting, page)
        else:
            result = self.movie_dao.get_all_movies(sorting, page)

        if result:
            return MovieSchema(many=True).dump(result), 200
        else:
            return {"message": "Movies into database not found"}, 404

    @handling_exceptions
    def add_movie(self, data):
        movie_dict = MovieSchema().load(data)
        movie = Movie(**movie_dict)
        self.movie_dao.create(movie)

        return {"message": f"Movie {Movie.title} added into database"}, 201

    @handling_exceptions
    def update_movie(self, data, mid):

        movie_dict = MovieSchema.load(data)
        self.movie_dao.update(movie_dict, mid)
        return {"message": f"Movie with ID: '{mid}' is updated"}, 204

    @handling_exceptions
    def delete_movie(self, mid):
        self.movie_dao.delete(mid)
        return {"message": f"Movie with ID: '{mid}' is deleted"}, 204
