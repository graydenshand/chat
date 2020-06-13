from flask_restful import Resource, fields
from flask import g, request, current_app
from ..models import User
from app import db, socketio, basic_auth, token_auth
from marshmallow import fields, Schema
from app.api.utilities.api import validate_with
from . import generate_token

class AuthInputSchema(Schema):
    email = fields.Email(required=True)
    password = fields.String(required=True)
    token = fields.String(required=True)

class AuthOutputSchema(Schema):
	token = fields.String(requred=True)

class Auth(Resource):
	"""
	Auth resource
	
	
	POST /channels.json
		* Request a new auth token
	PUT /channels.json
		* Restore token

	"""
	@validate_with(AuthInputSchema(partial=['token']))
	def post(self):
		"""
		Authorize email / password combination
		"""
		user = User.query.filter(User.email == g.validated_object['email']).first()
		if user and user.is_valid_password(g.validated_object['password']):
			token = generate_token(user)
			return AuthOutputSchema().dump({"token": token}), 201
		else:
			return {"errors": ['Invalid credentials']}, 403

	@validate_with(AuthInputSchema(partial=['email', 'password']))
	def put(self):
		"""
		Restore token
		"""
		return AuthOutputSchema().dump({"token": g.validated_object['token']}), 200
