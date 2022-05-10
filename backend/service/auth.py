from backend.dao.auth import AuthDao
from backend.tools.decorators import handling_exceptions
from backend.tools.secure import get_hash, create_tokens, decode_token


class AuthService:
    def __init__(self, dao: AuthDao):
        self.dao = dao

    @handling_exceptions
    def login(self, data):
        user = self.dao.get_user(data["email"], get_hash(data['password']))
        if user is not None:
            tokens = create_tokens({
                "email": user.email
            })
            return tokens

        else:
            return {"message": "Неверный email пользователя или пароль"}

    def get_new_tokens(self, token: str):

        decoded_token = decode_token(token)
        if decoded_token["refresh_token"]:
            tokens = create_tokens({
                "email": decoded_token["email"],
            })
            return tokens
