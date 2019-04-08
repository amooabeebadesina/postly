import os
from dotenv import load_dotenv
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_marshmallow import Marshmallow
from flask_bcrypt import Bcrypt

load_dotenv()
app = Flask(__name__)

app.config.from_object(os.getenv('APP_SETTINGS', 'config.DevelopmentConfig'))

db = SQLAlchemy(app)
migrate = Migrate(app, db)
marsh = Marshmallow(app)
bcrypt = Bcrypt(app)

from app.users.controllers import users_mod as users_module
app.register_blueprint(users_module)

@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404

db.create_all()