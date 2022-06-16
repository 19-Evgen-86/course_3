from flask import request
from flask_restx import Namespace, Resource

from schemas.base import UserSchema
from tools.implemented import auth_service, user_service
from tools.secure import get_token_from_headers
from tools.utils import convert_model

auth_ns = Namespace("auth")

user = auth_ns.model('user', convert_model(UserSchema()))

@auth_ns.route("/register/")
# регистрация пользователя
class AuthView(Resource):
    @auth_ns.expect(user)
    @auth_ns.response(200, description="Пользователь создан ")
    @auth_ns.response(404, description="Пользователь существует ")
    def post(self):
        return user_service.create(request.json)

@auth_ns.route("/login/")
class AuthView(Resource):
    # авторизация пользователя
    @auth_ns.expect(user)
    @auth_ns.response(200, description="Авторизация успешна")
    @auth_ns.response(404, description="Ошибка авторизации ")
    def post(self):
        return auth_service.login(request.json)

    # обновление токенов
    def put(self):
        token = get_token_from_headers(request.headers)
        return auth_service.get_new_tokens(token)
