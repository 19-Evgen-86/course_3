from flask import request
from flask_restx import Namespace, Resource

from backend.tools.implemented import auth_service, user_service
from backend.tools.secure import get_token_from_headers

auth_ns = Namespace("auth")


@auth_ns.route("/register/")
class AuthView(Resource):
    @auth_ns.doc(params={"email": "Почта пользователя", "password": "Пароль"})
    def post(self):
        return user_service.create(request.json)


@auth_ns.route("/login/")
class AuthView(Resource):
    @auth_ns.doc(params={"email": "Почта пользователя", "password": "Пароль"})
    def post(self):
        return auth_service.login(request.json)

    def put(self):
        data = get_token_from_headers(request.headers)
        return auth_service.get_new_tokens(data)
