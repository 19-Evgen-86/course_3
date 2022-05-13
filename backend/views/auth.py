from flask import request
from flask_restx import Namespace, Resource

from backend.tools.implemented import auth_service, user_service
from backend.tools.secure import get_token_from_headers

auth_ns = Namespace("auth")


@auth_ns.route("/register/")
# регистрация пользователя
class AuthView(Resource):

    def post(self):
        return user_service.create(request.json)

@auth_ns.route("/login/")
class AuthView(Resource):
    # авторизация пользователя
    def post(self):
        return auth_service.login(request.json)

    # обновление токенов
    def put(self):
        token = get_token_from_headers(request.headers)
        return auth_service.get_new_tokens(token)
