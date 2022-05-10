from flask import request
from flask_restx import Namespace, Resource

from backend.tools.implemented import genre_service

genre_ns = Namespace("genres")


@genre_ns.route("/")
class GenresView(Resource):

    def get(self):
        result = genre_service.get_genres_all(request.args)
        return result

    def post(self):
        data = request.json
        result = genre_service.add_genre(data)
        return result


@genre_ns.route("/<int:id>")
class GenresView(Resource):

    def get(self, id):
        result = genre_service.get_genre(id)
        return result

    def put(self, id):
        data = request.json
        result = genre_service.update_genre(data, id)
        return result, 201

    def delete(self, id):
        result = genre_service.delete_genre(id)
        return result
