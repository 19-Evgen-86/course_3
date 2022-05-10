from backend.dao.model.base import BaseModel
from backend.tools.setup_db import db


class Movie(BaseModel, db.Model):
    """
    Описывает модель таблицы фильмов
   """

    __tablename__ = 'movies'
    __table_args__ = {'extend_existing': True}
    title = db.Column(db.String(255), nullable=False)
    description = db.Column(db.String(255), nullable=False)
    trailer = db.Column(db.String(255), nullable=False)
    year = db.Column(db.Integer, nullable=False)
    rating = db.Column(db.Float, nullable=False)

    genre_id = db.Column(db.Integer, db.ForeignKey("genres.id"), nullable=False)
    director_id = db.Column(db.Integer, db.ForeignKey("directors.id"), nullable=False)

    director = db.relationship("Director")
    genre = db.relationship("Genre")
