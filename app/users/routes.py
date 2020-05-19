from flask_restful import Resource, reqparse, fields, marshal_with
from ..database.models import User
from ..database.base import db_session
from datetime import datetime

# Response schema definition
resource_fields = {
	'users': fields.Nested({
		'id': fields.Integer,
		'name': fields.String,
		'email': fields.String
	})
}

class Users(Resource):
	"""
	User resource
	
	GET
		* Returns list of messages if message id is not specified
		* Returns a single message if message id is specified
		* Returns messages by user_id if user_id is specified
	POST
		* Creates a new message
	PUT
		* Updates a message
	DELETE
		* Deletes a message
	"""
	pass
	
	@marshal_with(resource_fields)
	def get(self, user_id=None):
		"""
		Get one or many messages
		"""
		# User id is defined, return the user with the specified id
		if user_id:
			user = User.query.filter(User.id == user_id).first()
			return {"users":user}, 200
		# User id is not defined, return all users
		else:
			users = User.query.all()
			return {"users":users}, 200


	@marshal_with(resource_fields)
	def post(self):
		"""
		Create a new user
		"""

		# Validate input
		parser = reqparse.RequestParser()
		parser.add_argument('name', 'str', help="Couldn't format name")
		parser.add_argument('email', 'str', help="Couldn't format email")
		args = parser.parse_args()
		
		# Create user
		user_data = {
			"name": args['name'],
			"email": args['email'],
		}
		user = User(**user_data)

		# Save user to db
		db_session.add(user)
		db_session.commit()

		# Respond to client
		return {"users": user}, 201



	@marshal_with(resource_fields)
	def put(self, user_id):
		# Validate input
		parser = reqparse.RequestParser()
		parser.add_argument('name', 'str', help="Couldn't format name")
		parser.add_argument('email', 'str', help="Couldn't format email")
		args = parser.parse_args()

		# Update user
		user = User.query.filter(User.id == user_id).first()
		for k, v in args.items():
			setattr(user, k, v)
		db_session.add(user)
		db_session.commit()

		return {"users": user}, 200



	@marshal_with(resource_fields)
	def delete(self, user_id):

		# Update user
		user = User.query.filter(User.id == user_id).first()
		db_session.delete(user)
		db_session.commit()

		return {}, 204
