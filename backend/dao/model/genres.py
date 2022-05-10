from backend.dao.model.base import BaseModel
from backend.tools.setup_db import db


class Genre(BaseModel, db.Model):
    """
    Описывает модель таблицы жанров
   """

    __tablename__ = 'genres'
    __table_args__ = {'extend_existing': True}
    name = db.Column(db.String(100), unique=True, nullable=False)
