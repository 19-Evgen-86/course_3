# файл для создания DAO и сервисов чтобы импортировать их везде
from dao.auth import AuthDao
from dao.director import DirectorDao
from dao.favorites import FavoritesDao
from dao.genre import GenreDao
from dao.movie import MovieDao
from dao.user import UserDao
from service.auth import AuthService
from service.director import DirectorService
from service.favorites import FavoritesService
from service.genre import GenreService
from service.movie import MovieService
from service.user import UserService
from tools.setup_db import db

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

favorites_movies_dao = FavoritesDao(db.session)
favorites_movies_service = FavoritesService(favorites_movies_dao)
