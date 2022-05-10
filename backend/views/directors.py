from flask import request
from flask_restx import Namespace, Resource

from backend.tools.implemented import director_service

director_ns = Namespace("directors")


@director_ns.route("/")
class DirectorsView(Resource):

    def get(self):
        result = director_service.get_director_all(request.args)
        return result

    def post(self):
        data = request.json
        result = director_service.add_director(data)
        return result


@director_ns.route("/<int:id>")
class DirectorView(Resource):

    def get(self, id):
        result = director_service.get_director(id)
        return result

    def put(self, id):
        data = request.json
        result = director_service.update_movie(data, id)
        return result

    def delete(self, id):
        result = director_service.delete_movie(id)
        return result
