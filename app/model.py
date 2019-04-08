import os
from app import db, marsh
from hashids import Hashids

hasher = Hashids(os.getenv('HASH_SALT'), min_length=8)
class BaseModel(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    created_at = db.Column(db.DateTime, auto_now_add=True)

    @property
    def idd(self):
        return hasher.encode(self.id)