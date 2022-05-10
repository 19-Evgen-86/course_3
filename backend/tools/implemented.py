# файл для создания DAO и сервисов чтобы импортировать их везде
from backend.dao.auth import AuthDao
from backend.dao.director import DirectorDao
from backend.dao.genre import GenreDao
from backend.dao.movie import MovieDao
from backend.dao.user import UserDao
from backend.service.auth import AuthService
from backend.service.director import DirectorService
from backend.service.genre import GenreService
from backend.service.movie import MovieService
from backend.service.user import UserService
from backend.tools.setup_db import db

movie_dao = MovieDao(db.session)
movie_service = MovieService(movie_dao)

director_dao = DirectorDao(db.session)
director_service = DirectorService(director_dao)

genre_dao = GenreDao(db.session)
genre_service = GenreService(genre_dao)

user_dao = UserDao(db.session)
user_service = UserService(user_dao)

auth_dao = AuthDao(db.session)
auth_service = AuthService(auth_dao)

