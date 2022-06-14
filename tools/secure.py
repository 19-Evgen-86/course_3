import base64
import hashlib
import hmac
from datetime import datetime, timedelta

import jwt
from flask import current_app
from flask_restx import abort


def get_hash(password):
    """
    саздает Хэш пароля
    :param password:
    :return:
    """
    hash: bytes = hashlib.pbkdf2_hmac(
        current_app.config['PWD_HASH_NAME'],
        password.encode('utf-8'),  # Convert the password to bytes
        current_app.config['PWD_HASH_SALT'],
        current_app.config['PWD_HASH_ITERATIONS']
    )

    return base64.b64encode(hash).decode("utf-8")


def create_tokens(data: dict) -> dict:
    """
    создает токен для пользователя data['username']
    :param data:
    :return:
    """
    data["exp"] = datetime.utcnow() + timedelta(minutes=30)
    data["refresh_token"] = False
    access_token: str = jwt.encode(data, current_app.config['SECRET_KEY'], algorithm=current_app.config['ALGO'])

    data["exp"] = datetime.utcnow() + timedelta(days=30)
    data["refresh_token"] = True
    refresh_token: str = jwt.encode(data, current_app.config['SECRET_KEY'], algorithm=current_app.config['ALGO'])

    return {
        "access_token": access_token,
        "refresh_token": refresh_token
    }


def get_token_from_headers(headers: dict):
    """
    получаем токен из заголовка
    :param headers:
    :return:
    """
    if "Authorization" not in headers:
        abort(401, message="Необходима авторизация")
    return headers['Authorization'].split(' ')[-1]


def decode_token(token: str):
    """
    декодирует токен
    :param token:
    :param refresh_token:
    :return:
    """
    decoded_token: dict = {}
    try:
        decoded_token = jwt.decode(token, current_app.config['SECRET_KEY'], current_app.config['ALGO'])
    except jwt.PyJWTError as exc:
        abort(401, message=f"error {exc}")

    return decoded_token


def compare_pwd(pwd_1, pwd_2):
    return hmac.compare_digest(pwd_1, pwd_2)
