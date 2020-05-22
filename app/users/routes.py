from flask_restful import Resource, fields
from ..database.models import User
from ..database.base import Db
from datetime import datetime
from app.utilities.api import validate_with

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
			users = User.query.all()
			return {"users": User.schema(many=True).dump(users)}, 200

	@validate_with(User.schema())
	def post(self):
		"""
		Create a new user
		"""
		# Create user
		user_data = {
			"name": args['name'],
			"email": args['email'],
		}
		user = User(**user_data)

		# Save user to db
		Db.session.add(user)
		Db.session.commit()

		# Respond to client
		return {"users": User.schema().dump(user)}, 201


	@validate_with(User.schema)
	def put(self, user_id):

		# Update user
		user = User.query.filter(User.id == user_id).first()
		for k, v in args.items():
			setattr(user, k, v)
		Db.session.add(user)
		Db.session.commit()

		return {"users": User.schema().dump(user)}, 200



	def delete(self, user_id):

		# Update user
		user = User.query.filter(User.id == user_id).first()
		Db.session.delete(user)
		Db.session.commit()

		return {}, 204
