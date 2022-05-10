from backend.dao.director import DirectorDao
from backend.dao.model.directors import Director
from backend.schemas.base import DirectorSchema
from backend.tools.decorators import handling_exceptions


class DirectorService:
    def __init__(self, director_dao: DirectorDao):
        self.director_dao = director_dao

    @handling_exceptions
    def get_director_all(self, param):
        if "page" in param:
            result = self.director_dao.get_all(param["page"])
        else:
            result = self.director_dao.get_all()
        if result:
            return DirectorSchema(many=True).dump(result)
        else:
            return {"message": "Genres into database not found"}

    @handling_exceptions
    def get_director(self, did):
        result = self.director_dao.get_one(did)
        if result:
            return DirectorSchema().dump(result)
        else:
            return {"message": f"Genre with ID: '{did}' not found"}

    @handling_exceptions
    def add_director(self, data):
        director_dict = DirectorSchema().load(data)
        director = Director(**director_dict)
        self.director_dao.create(director)

        return {"message": f"director {Director.name} added into database"}

    @handling_exceptions
    def update_movie(self, data, did):

        director_dict = DirectorSchema().load(data)
        self.director_dao.update(director_dict, did)
        return {"message": f"Director with ID: '{did}' is updated"}

    @handling_exceptions
    def delete_movie(self, did):
        self.director_dao.delete(did)
        return {"message": f"Director with ID: '{did}' is deleted"}
