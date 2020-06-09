from flask import Blueprint, current_app
from app import db, socketio, basic_auth, token_auth
from app.models import User
from flask_restful import Api, Resource
import jwt

def generate_token(user):
	token = jwt.encode(user.schema(only=["id", "email"]).dump(user), current_app.config['SECRET_KEY'], algorithm='HS256')
	return token

@token_auth.verify_token
def verify_token(token):
	print(token)
	try:
		data = jwt.decode(token, current_app.config['SECRET_KEY'], algorithm="HS256")
	except:  # noqa: E722
		return False
	if 'id' in data:
		print(data)
		return User.query.get(data['id'])

@basic_auth.verify_password
def verify_password(email, password):
	user = User.query.filter(User.email == email).first()
	if user and user.validate_password(password):
		return user

@basic_auth.error_handler
def auth_error(status):
	return {"errors": ["Unauthorized access please check your api credentials"]}, status


auth = Blueprint('auth', __name__)
api = Api(auth)

# avoid circular import errors
from app.auth import routes

api.add_resource(routes.Auth, '/auth.json')