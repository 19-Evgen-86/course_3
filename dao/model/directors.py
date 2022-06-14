
from dao.model.base import BaseModel
from tools.setup_db import db


class Director(BaseModel, db.Model):
    """
     Описывает модель таблицы режиссеров
    """
    __tablename__ = 'directors'
    __table_args__ = {'extend_existing': True}
    name = db.Column(db.String(100), unique=True, nullable=False)



