# Это файл конфигурации приложения, здесь может хранится путь к бд, ключ шифрования, что-то еще.
# Чтобы добавить новую настройку, допишите ее в класс.
import os

DATABASE_PATH = os.path.join(os.getcwd(), "base.db")
PAGE_SIZE =12

class Config:
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = f'sqlite:///{DATABASE_PATH}'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JSON_AS_ASCII = False
    PWD_HASH_SALT = b'secret here'
    PWD_HASH_ITERATIONS = 100_000
    PWD_HASH_NAME = 'sha256'
    SECRET_KEY = "s3cR$eT"
    ALGO = 'HS256'
    TOKEN_EXPIRE_MINUTES = 15
    TOKEN_EXPIRE_DAYS = 130
    RESTX_MASK_SWAGGER = False