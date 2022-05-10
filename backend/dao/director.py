from backend.config import PAGE_SIZE
from backend.dao.model.directors import Director


class DirectorDao():
    """
    Класс для взаимодействия c таблицей режиссеров в БД
    """

    def __init__(self, session):
        self.session = session

    def get_all(self,page:int = 0):
        if page > 0:
            return self.session.query(Director).limit(PAGE_SIZE).offset(page * PAGE_SIZE).all()
        return self.session.query(Director).all()

    def get_one(self, mid):
        return self.session.query(Director).get(mid)

    def create(self, data):
        with self.session.begin():
            self.session.add(data)

    def update(self, data, mid):
        with self.session.begin():
            self.session.query(Director).filter(Director.id == mid).update(data)

    def delete(self, mid):
        with self.session.begin():
            self.session.query(Director).filter(Director.id == mid).delete()