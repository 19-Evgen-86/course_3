from dao.model.user import User


class UserDao:
    def __init__(self, session):
        self.session = session

    def create(self, data: User):
        with self.session.begin():
            self.session.add(data)

    def update(self, data: dict, email: str):
        with self.session.begin():
            self.session.query(User).filter(User.email == email).update(data)

    def get(self, email):
        return self.session.query(User).filter(User.email == email).first()

    def get_pwd(self, email):
        with self.session.begin():
            return self.session.query(User.password).filter(User.email == email).first()
