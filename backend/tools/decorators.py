from functools import wraps

from flask import request, abort

from backend.tools.secure import get_token_from_headers, decode_token


def handling_exceptions(func):
    """
    отлавливает возможные ошибки
    используется в качестве декоратора
    :param func:
    :return:
    """

    @wraps(func)
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as ex:
            return {"error ": ex.__repr__()}, 404

    return inner


def auth_required(func):
    @wraps(func)
    def inner(*args, **kwargs):
        token = get_token_from_headers(request.headers)
        decode_token(token)
        return func(*args, **kwargs)


    return inner
