from flask import request
from flask_restx import Namespace, Resource

from backend.tools.implemented import genre_service

genre_ns = Namespace("genres")


@genre_ns.route("/")
class GenresView(Resource):
    @genre_ns.response(200, description="Возвращает список всех жанров")
    @genre_ns.doc(params={"page": "Номер страницы"})
    def get(self):
        result = genre_service.get_genres_all(request.args)
        return result, 200

    @genre_ns.response(200, description="Фильм добавлен")
    def post(self):
        data = request.json
        result = genre_service.add_genre(data)
        return result, 200


@genre_ns.route("/<int:id>")
class GenresView(Resource):
    @genre_ns.param("id", "ID Жанра")
    @genre_ns.response(200, description="Возвращает данные жанра по ID")
    def get(self, id):
        result = genre_service.get_genre(id)
        return result, 200

    @genre_ns.doc(params={"id": "ID Жанра", "data": "Данные для обновления"})
    @genre_ns.response(201, description="Жанр обновлен")
    def put(self, id):
        data = request.json
        result = genre_service.update_genre(data, id)
        return result, 201

    @genre_ns.param("id", "ID Жанра")
    @genre_ns.response(204, description="Жанр удален")
    def delete(self, id):
        result = genre_service.delete_genre(id)
        return result, 204
