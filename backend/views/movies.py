from flask import request
from flask_restx import Namespace, Resource

from backend.tools.implemented import movie_service

movie_ns = Namespace("movies")


@movie_ns.route("/")
class MoviesView(Resource):

    def get(self):
        result = movie_service.get_movie_all(request.args)
        return result

    def post(self):
        data = request.json
        result = movie_service.add_movie(data)
        return result, 200


@movie_ns.route("/<int:id>")
class MovieView(Resource):

    def get(self, id):
        result = movie_service.get_movie_one(id)
        return result, 200

    def put(self, id):
        data = request.json
        result = movie_service.update_movie(data, id)
        return result, 201

    def delete(self, id):
        result = movie_service.delete_movie(id)
        return result, 204
