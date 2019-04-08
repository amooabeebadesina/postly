from app import db, marsh, bcrypt
from app.model import BaseModel

class User(BaseModel):
    __tablename__ = 'users'
    
    first_name = db.Column(db.String(64))
    last_name = db.Column(db.String(64))
    email = db.Column(db.String(120), unique=True, index=True)
    password = db.Column(db.String(191))

    def __init__(self, first_name, last_name, email, password):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = bcrypt.generate_password_hash(password)

class UserSchema(marsh.ModelSchema):
    class Meta:
        fields = ("idd", "email", "first_name", "last_name", "created_at")