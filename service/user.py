from dao.model.user import User
from dao.user import UserDao
from schemas.base import UserSchema
from tools.decorators import handling_exceptions
from tools.secure import get_hash, decode_token, compare_pwd


class UserService:

    def __init__(self, dao: UserDao):
        self.dao = dao

    @handling_exceptions
    def get(self, token: str):

        email = decode_token(token)["email"]
        result = self.dao.get(email)
        if result:
            return UserSchema().dump(result)
        else:
            return {"message": "Пользователь не найден"}, 404

    @handling_exceptions
    def create(self, data):
        valid_user = UserSchema().load(data=data)
        valid_user["password"] = get_hash(valid_user["password"])
        user = User(**valid_user)
        self.dao.create(user)
        return {"message": "Пользователь создан"}, 200

    @handling_exceptions
    def update(self, data):
        data_update = {}

        if data['method'] == "patch":
            email = decode_token(data['token'])["email"]
            if "name" in data:
                data_update['name'] = data['name']
            if 'surname' in data:
                data_update["surname"] = data["surname"]
            if 'favourite_genre' in data:
                data_update['favorite_genre'] = data['favourite_genre']
            self.dao.update(data_update, email)
            return {"message": "данные обновлены"}, 201

        elif data['method'] == "put":
            email = decode_token(data['token'])["email"]
            # создаем хеш пароля переданного пользователем
            old_pwd = get_hash(data["old_password"])
            # получаем хэш пароля из базы
            user_pwd = self.dao.get_pwd(email)[0]
            # сравниваем полученные хеши
            if compare_pwd(user_pwd, old_pwd):
                # если они совпадают, то сохраняем новый пароль
                data_update['password'] = get_hash(data["new_password"])
                self.dao.update(data_update, email)

                return {"message": "пароль обновлен"}, 201
            else:
                # если не совпадают возвращаем ошибку
                return {"error": "неверный пароль"}, 404

