from backend.dao.genre import GenreDao
from backend.dao.model.genres import Genre
from backend.schemas.base import GenreSchema
from backend.tools.decorators import handling_exceptions

genre_schemas = GenreSchema(many=True)
genre_schema = GenreSchema()


class GenreService:
    def __init__(self, genre_dao: GenreDao):
        self.genre_dao = genre_dao

    @handling_exceptions
    def get_genres_all(self, param: dict):

        if "page" in param:
            result = self.genre_dao.get_all(param["page"])
        else:
            result = self.genre_dao.get_all()
        if result:
            return GenreSchema(many=True).dump(result), 200
        else:
            return {"message": "Genres into database not found"}, 404

    @handling_exceptions
    def get_genre(self, gid):
        result = self.genre_dao.get_one(gid)
        if result:
            return GenreSchema().dump(result), 200
        else:
            return {"message": f"Genre with ID: '{gid}' not found"}, 404

    @handling_exceptions
    def add_genre(self, data):
        genre_dict = GenreSchema().load(data)
        genre = Genre(**genre_dict)
        self.genre_dao.create(genre)

        return {"message": f"Genre {Genre.title} added into database"}, 200

    @handling_exceptions
    def update_genre(self, data, gid):

        genre_dict = GenreSchema().load(data)
        self.genre_dao.update(genre_dict, gid)
        return {"message": f"Genre with ID: '{gid}' is updated"}, 201

    @handling_exceptions
    def delete_genre(self, gid):
        self.genre_dao.delete(gid)
        return {"message": f"Genre with ID: '{gid}' is deleted"}, 204
