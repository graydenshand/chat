from flask_restful import Resource, reqparse
from ..database.models import Message

class MessageResource(Resource):
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
	def get(self, message_id=None):
		parser = reqparse.RequestParser()
		parser.add_argument('message_id', 'int', help="Couldn't format user.id")
		args = parser.parse_args()

		if message_id:
			msg = Message.query.filter(Message.id == message_id).first()
			return {'data': {"message": msg.message, "user_id": msg.user_id}}
		messages = Message.query.all()
		return {'data': [{"message": msg.message, "user_id": msg.user_id} for msg in messages]}