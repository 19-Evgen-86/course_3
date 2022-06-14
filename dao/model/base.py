from tools.setup_db import db


class BaseModel:
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)

