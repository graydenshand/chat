from flask_restful import Resource, fields
from flask import g
from ..models import User
from app import db
from datetime import datetime
from app.utilities.api import validate_with
from app import socketio

class Users(Resource):
	"""
	User resource
	
	GET
		* Returns list of users if user id is not specified
		* Returns a single user if user id is specified
	POST
		* Creates a new user
	PUT
		* Updates a user
	DELETE
		* Deletes a user
	"""
	
	def get(self, user_id=None):
		"""
		Get one or many messages
		"""
		# User id is defined, return the user with the specified id
		if user_id:
			user = User.query.filter(User.id == user_id).first()
			return {"users": User.schema().dump(user)}, 200
		# User id is not defined, return all users
		else:
			socketio.emit("message", "Get Users")
			users = User.query.all()
			return {"users": User.schema(many=True).dump(users)}, 200

	@validate_with(User.schema())
	def post(self):
		"""
		Create a new user
		"""
		# Create user
		user = g.validated_object

		# Save user to db
		db.session.add(user)
		db.session.commit()

		# Respond to client
		return {"users": User.schema().dump(user)}, 201


	@validate_with(User.schema())
	def put(self, user_id):

		# Update user
		user = User.query.filter(User.id == user_id).first()
		for k, v in request.json.items():
			setattr(user, k, v)
		db.session.add(user)
		db.session.commit()

		return {"users": User.schema().dump(user)}, 200



	def delete(self, user_id):

		# Update user
		user = User.query.filter(User.id == user_id).first()
		db.session.delete(user)
		db.session.commit()

		return {}, 204
