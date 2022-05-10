from flask import request
from flask_restx import Namespace, Resource

from backend.tools.implemented import movie_service

movie_ns = Namespace("movies")


@movie_ns.route("/")
class MoviesView(Resource):
    @movie_ns.doc(params={"director_id": "ID Режиссера", "genre_id": "ID :Жанра",
                          "status": "New (показать новинки)", "page": "Номер страницы"})
    @movie_ns.response(200, description="Возвращает список фильмов")
    def get(self):
        result = movie_service.get_movie_all(request.args)
        return result, 200

    @movie_ns.response(200, description="Фильм добавлен")
    def post(self):
        data = request.json
        result = movie_service.add_movie(data)
        return result, 200


@movie_ns.route("/<int:id>")
class MovieView(Resource):
    @movie_ns.doc(params={"id": "ID Фильма"})
    @movie_ns.response(200, description="Возвращает фильм по ID")
    def get(self, id):
        result = movie_service.get_movie_one(id)
        return result, 200

    @movie_ns.doc(params={"id": "ID Фильма", "data": "Данные для обновления"})
    @movie_ns.response(201, description="Фильм обновлен")
    def put(self, id):
        data = request.json
        result = movie_service.update_movie(data, id)
        return result, 201

    @movie_ns.param("id", "ID Фильма")
    @movie_ns.response(204, description="Фильм удален")
    def delete(self, id):
        result = movie_service.delete_movie(id)
        return result, 204
