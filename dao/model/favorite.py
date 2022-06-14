from tools.setup_db import db


# class Favorite(db.Model):
#     __tablename__ = 'favorites'
#     __table_args__ = {'extend_existing': True}
#
#     user_id = db.Column(db.Integer, db.ForeignKey("users.id"), primary_key=True)
#     movie_id = db.Column(db.Integer, db.ForeignKey("movies.id"), primary_key=True)

favorites = db.Table('favorites',
                     db.Column('user_id', db.Integer, db.ForeignKey('users.id'), primary_key=True),
                     db.Column('movie_id', db.Integer, db.ForeignKey('movies.id'), primary_key=True)
                     )
