from flask import request
from flask_restx import Namespace, Resource

from schemas.base import GenreSchema
from utilites.implemented import genre_service
from utilites.utils import convert_model

genre_ns = Namespace("genres")

genres = genre_ns.model("genres", convert_model(GenreSchema()))


@genre_ns.route("/")
class GenresView(Resource):

    @genre_ns.response(200, description="Получен список жанров ")
    @genre_ns.response(404, description="Данных в БД о жанрах нет")
    def get(self):
        result = genre_service.get_genres_all(request.args)
        return result

    @genre_ns.response(201, description="Жанр добавлен ")
    @genre_ns.response(404, description="Ошибка при добавлении жанра")
    @genre_ns.marshal_with(genres)
    def post(self):
        data = request.json
        result = genre_service.add_genre(data)
        return result


@genre_ns.route("/<int:id>")
class GenresView(Resource):
    @genre_ns.response(200, description="Данные о жанре по ID ")
    @genre_ns.response(404, description="Жанр по ID не найден")
    def get(self, id):
        result = genre_service.get_genre(id)
        return result

    @genre_ns.response(204, description="Жанр обновлен ")
    @genre_ns.response(404, description="Ошибка при обновлении жанра")
    @genre_ns.marshal_with(genres)
    def put(self, id):
        data = request.json
        result = genre_service.update_genre(data, id)
        return result

    @genre_ns.response(204, description="Данные о жанре удалены ")
    @genre_ns.response(404, description="Ошибка при удалении жанра")
    def delete(self, id):
        result = genre_service.delete_genre(id)
        return result
