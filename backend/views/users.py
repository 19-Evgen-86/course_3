from flask import request
from flask_restx import Resource, Namespace

from backend.tools.decorators import auth_required
from backend.tools.implemented import user_service
from backend.tools.secure import get_token_from_headers

user_ns = Namespace('user')


@user_ns.route("/")
class UserView(Resource):
    @auth_required
    def get(self):
        token = get_token_from_headers(request.headers)
        result = user_service.get(token)
        return result, 200

    @auth_required
    def patch(self):
        data = request.json
        data["method"] = 'patch'
        data['token'] = get_token_from_headers(request.headers)
        result = user_service.update(data)
        return result, 200


@user_ns.route("/password/")
class UserView(Resource):
    @auth_required
    def put(self):
        data = request.json
        data["method"] = 'put'
        data['token'] = get_token_from_headers(request.headers)
        result = user_service.update(data)
        return result
