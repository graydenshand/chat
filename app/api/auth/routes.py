from flask_restful import Resource, fields
from flask import g, request, current_app
from ..models import User
from app import db, socketio, basic_auth, token_auth
from marshmallow import fields, Schema
from app.api.utilities.api import validate_with
from . import generate_token, verify_token

class AuthInputSchema(Schema):
	id = fields.Integer()
	email = fields.Email(required=True)
	password = fields.String(required=True)
	token = fields.String(required=True)

class AuthOutputSchema(Schema):
	token = fields.String(requred=True)
	id = fields.Integer(required=True)
	name = fields.String(required=True)
	email = fields.Email(required=True)


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
			return AuthOutputSchema().dump({"token": token, "id": user.id}), 201
		else:
			return {"errors": ['Invalid credentials']}, 403

	@validate_with(AuthInputSchema(partial=['email', 'password']))
	def put(self):
		"""
		Validate session
		"""
		user = verify_token(g.validated_object['token'])
		return AuthOutputSchema().dump({"token": g.validated_object['token'], "id": user.id,}), 200
