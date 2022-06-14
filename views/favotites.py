from flask import request
from flask_restx import Namespace, Resource

from tools.decorators import auth_required
from tools.implemented import favorites_movies_service
from tools.secure import get_token_from_headers

favorites_ns = Namespace("favorites")

@favorites_ns.route("/movies/<int:id>")
class FavoritesView(Resource):
    @auth_required
    def post(self, id):
        token = get_token_from_headers(request.headers)
        result = favorites_movies_service.add(id, token)

        return result

    @auth_required
    def delete(self, id):
        token = get_token_from_headers(request.headers)
        result = favorites_movies_service.delete(id, token)
        return result
