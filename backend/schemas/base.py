from marshmallow import Schema, fields


class UserSchema(Schema):
    id = fields.Int(dump_only=True, required=True)
    name = fields.Str()
    surname = fields.Str()
    password = fields.Str(required=True)
    role = fields.Str()
    email = fields.Str(required=True)
    favorite_genre = fields.Str()


class MovieSchema(Schema):
    """
   Схема для сериализация
   """

    id = fields.Int(dump_only=True, required=True)
    title = fields.Str(required=True)
    description = fields.Str(required=True)
    trailer = fields.Str(required=True)
    year = fields.Int(required=True)
    rating = fields.Float(required=True)
    genre_id = fields.Int(required=True)
    director_id = fields.Int(required=True)


class DirectorSchema(Schema):
    """
    Схема для сериализация
    """
    id = fields.Int(dump_only=True, required=True)
    name = fields.Str(required=True)


class GenreSchema(Schema):
    """
   Схема для сериализация
   """

    id = fields.Int(dump_only=True, required=True)
    name = fields.Str(required=True)
