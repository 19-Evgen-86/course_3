from flask import request
from flask_restx import Namespace, Resource

from schemas.base import MovieSchema
from tools.implemented import movie_service
from tools.utils import convert_model

movie_ns = Namespace("movies")
movies = movie_ns.model("movies", convert_model(MovieSchema()))


@movie_ns.route("/")
class MoviesView(Resource):

    @movie_ns.response(200, description="Получен список фильмов ")
    @movie_ns.response(404, description="Данных в БД о фильмах нет")
    def get(self):
        result = movie_service.get_movie_all(request.args)
        return result

    @movie_ns.response(201, description="Фильм добавлен ")
    @movie_ns.response(404, description="Ошибка при добавлении фильма")
    @movie_ns.marshal_with(movies)
    def post(self):
        data = request.json
        result = movie_service.add_movie(data)
        return result


@movie_ns.route("/<int:id>")
class MovieView(Resource):
    @movie_ns.response(200, description="Получен фильм по ID ")
    @movie_ns.response(404, description="Фильм по ID не найден")
    def get(self, id):
        result = movie_service.get_movie_one(id)
        return result

    @movie_ns.response(204, description="Данные о фильме обновлены ")
    @movie_ns.response(404, description="Ошибка при обновлении фильма")
    @movie_ns.marshal_with(movies)
    def put(self, id):
        data = request.json
        result = movie_service.update_movie(data, id)
        return result

    @movie_ns.response(204, description="Данные о фильме удалены ")
    @movie_ns.response(404, description="Ошибка при удалении фильма")
    def delete(self, id):
        result = movie_service.delete_movie(id)
        return result
