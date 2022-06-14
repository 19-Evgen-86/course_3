from dao.model.user import User


class AuthDao:
    def __init__(self, session):
        self.session = session

    def get_user(self, email, password):
        return self.session.query(User).filter(User.email == email, User.password == password).first()

