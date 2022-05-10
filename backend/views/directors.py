from flask import request
from flask_restx import Namespace, Resource

from backend.tools.implemented import director_service


director_ns = Namespace("directors")


@director_ns.route("/")
class DirectorsView(Resource):
    @director_ns.response(200, description="Возвращает список всех режиссеров")
    @director_ns.doc(params={"page": "Номер страницы"})
    def get(self):
        result = director_service.get_director_all(request.args)
        return result, 200

    @director_ns.response(200, description="Режиссер добавлен")

    def post(self):
        data = request.json
        result = director_service.add_director(data)
        return result, 200


@director_ns.route("/<int:id>")
class DirectorView(Resource):
    @director_ns.param("id", "ID Режиссера")
    @director_ns.response(200, description="Возвращает данные режиссера по ID")

    def get(self, id):
        result = director_service.get_director(id)
        return result, 200

    @director_ns.doc(params={"id": "ID Режиссера", "data": "Данные для обновления"})
    @director_ns.response(201, description="Режиссер обновлен")

    def put(self, did):
        data = request.json
        result = director_service.update_movie(data, did)
        return result, 201

    @director_ns.param("id", "ID Режиссер")
    @director_ns.response(204, description="Режиссер удален")

    def delete(self, id):
        result = director_service.delete_movie(id)
        return result, 204
