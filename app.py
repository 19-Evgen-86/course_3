# основной файл приложения. здесь конфигурируется фласк, сервисы, SQLAlchemy и все остальное что требуется для приложения.
# этот файл часто является точкой входа в приложение

from flask import Flask
from flask_cors import CORS
from flask_restx import Api, fields

from tools.setup_db import db
from views.favotites import favorites_ns
from config import Config
from insert_database_data import create_data
from views.auth import auth_ns
from views.directors import director_ns
from views.genres import genre_ns
from views.movies import movie_ns
from views.users import user_ns
from distutils.sysconfig import get_python_lib

# функция создания основного объекта app
def create_app(config_object):
    app = Flask(__name__)
    CORS(app)
    app.config.from_object(config_object)
    register_extensions(app)
    return app


# функция подключения расширений (Flask-SQLAlchemy, Flask-RESTx, ...)
def register_extensions(app):
    db.init_app(app)
    with app.app_context():
        db.create_all()
        create_data(db)

    api = Api(app, doc="/docs")

    api.add_namespace(director_ns)
    api.add_namespace(movie_ns)
    api.add_namespace(genre_ns)
    api.add_namespace(user_ns)
    api.add_namespace(auth_ns)
    api.add_namespace(favorites_ns)


app = create_app(Config())


if __name__ == '__main__':
        app.run()



