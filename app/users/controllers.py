from app import app, db
from flask import jsonify, request, Blueprint

from app.users.models import User, UserSchema
from app.utils.response import JSONResponse
from app.utils.validators import validate_create_user

user_schema = UserSchema()
users_mod = Blueprint('users', __name__, url_prefix="/users")

@users_mod.route('/', methods=['POST', 'GET'])
def users():
    if request.method == 'POST':
        data = request.get_json()
        if validate_create_user(data):
            existing_user = User.query.filter_by(email = data['email']).first()
            if existing_user is not None:
                return JSONResponse.sendErrorResponse('User already exists', 403)
            new_user = User(data['first_name'],data['last_name'],data['email'],data['password'])
            db.session.add(new_user)
            db.session.commit()
            result = user_schema.dumps(User.query.filter_by(email = data['email']).first()).data
            return JSONResponse.sendSuccessResponse(result, 201)
        return JSONResponse.sendErrorResponse('Bad request body', 400)
    else:
        users = User.query.all()
        return JSONResponse.sendSuccessResponse(users)

@users_mod.route('/<id>', methods=['GET'])
def get_user_details(id):
    user = User.query.filter_by(id=id).first()
    print (user)
    if user is None:
        return JSONResponse.sendErrorResponse('User does not exist')
    result = user_schema.dumps(user).data
    return JSONResponse.sendSuccessResponse(result)