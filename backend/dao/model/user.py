from backend.dao.model.base import BaseModel
from backend.tools.setup_db import db


class User(BaseModel, db.Model):
    __tablename__ = 'users'
    __table_args__ = {'extend_existing': True}
    name = db.Column(db.String(100))
    surname = db.Column(db.String(100))
    email = db.Column(db.String(100), nullable=False)
    password = db.Column(db.String(255), nullable=False)
    favorite_genre = db.Column(db.Integer, db.ForeignKey("genres.id"))
    # favorite_id = db.Column(db.Integer, db.ForeignKey("favorites.id"))

    favorite = db.relationship("Genre")
