from backend.dao.model.base import BaseModel
from backend.tools.setup_db import db


class Favorite(BaseModel, db.Model):
    __tablename__ = 'favorites'
    __table_args__ = {'extend_existing': True}

    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    movie_id = db.Column(db.Integer, db.ForeignKey("movies.id"))

    user = db.relationship("User")
    movie = db.relationship("Movie")
