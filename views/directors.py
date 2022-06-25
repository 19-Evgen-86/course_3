from flask import request
from flask_restx import Namespace, Resource

from schemas.base import DirectorSchema
from utilites.implemented import director_service
from utilites.utils import convert_model

director_ns = Namespace("directors")

directors = director_ns.model('directors', convert_model(DirectorSchema()))


@director_ns.route("/")
class DirectorsView(Resource):
    @director_ns.response(200, description="Получен список режиссеров ")
    @director_ns.response(404, description="Данных в БД о режиссерах нет")
    @director_ns.marshal_with(directors)
    def get(self):
        result = director_service.get_director_all(request.args)
        return result

    @director_ns.response(201, description="Режиссер добавлен ")
    @director_ns.response(404, description="Ошибка при добавлении")
    @director_ns.expect(directors)
    def post(self):
        data = request.json
        result = director_service.add_director(data)
        return result


@director_ns.route("/<int:id>")
class DirectorView(Resource):
    @director_ns.response(200, description="Полученны данные о режиссере по ID")
    @director_ns.response(404, description="Режиссер по ID  не найден ")
    @director_ns.marshal_with(directors)
    def get(self, id):
        result = director_service.get_director(id)
        return result

    @director_ns.response(204, description="данные о режиссере обновлены ")
    @director_ns.response(404, description="Ошибка при обновлении")
    @director_ns.expect(directors)
    def put(self, id):
        data = request.json
        result = director_service.update(data, id)
        return result

    @director_ns.response(204, description="данные о режиссере удалены ")
    @director_ns.response(404, description="Ошибка при удалении")
    def delete(self, id):
        result = director_service.delete(id)
        return result
