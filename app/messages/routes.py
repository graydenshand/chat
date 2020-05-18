from flask_restful import Resource, reqparse, fields, marshal_with
from ..database.models import Message
from ..database.base import db_session
from datetime import datetime

resource_fields = {
	'messages': fields.Nested({
		'id': fields.Integer,
		'message': fields.String,
		'createdAt': fields.DateTime(attribute='created_at'),
		'userId': fields.Integer(attribute="user_id")
	})
}

class Messages(Resource):
	"""
	Message resource
	
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


	@marshal_with(resource_fields)
	def get(self, message_id=None):
		"""
		Get one or many messages
		"""
		# Message id is defined, return the message with the specified id
		if message_id:
			message = Message.query.filter(Message.id == message_id).first()
			return {"messages":message}, 200
		# Message id is not defined, return all messages
		else:
			messages = Message.query.all()
			return {"messages":messages}, 200



	@marshal_with(resource_fields)
	def post(self):
		"""
		Create a new message
		"""

		# Validate input
		parser = reqparse.RequestParser()
		parser.add_argument('message', 'str', help="Couldn't format message text")
		parser.add_argument('userId', 'int', help="Couldn't format userId")
		args = parser.parse_args()
		
		# Create message
		message_data = {
			"user_id": args['userId'],
			"message": args['message'],
			'created_at': datetime.now()
		}
		message = Message(**message_data)

		# Save message to db
		db_session.add(message)
		db_session.commit()

		# Respond to client
		return {"messages": message}, 200

	@marshal_with(resource_fields)
	def put(self, message_id=None):
		# Validate input
		parser = reqparse.RequestParser()
		parser.add_argument('message', 'str', help="Couldn't format message text")
		parser.add_argument('userId', 'int', help="Couldn't format userId")
		parser.add_argument('createdAt', 'datetime', help="Couldn't format createdAt")
		args = parser.parse_args()

		# Update message
		message = Message.query.filter(Message.id == message_id).first()
		for k, v in args.items():
			setattr(message, k, v)
		db_session.add(message)
		db_session.commit()

		return {"messages": message}, 200


