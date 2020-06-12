from flask import request, g
from flask_restful import Resource, fields, abort
from ..models import Message
from app import db, auth
from datetime import datetime
from marshmallow import ValidationError
from app.api.utilities.api import validate_with

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

	@auth.login_required
	@validate_with(Message.schema(only=["user_id", "channel_id"], partial=True))
	def get(self, message_id=None):
		"""
		Get one or many messages
		"""
		# Message id is defined, return the message with the specified id
		if message_id:
			message = Message.query.get(message_id)
			return {"messages": Message.schema().dump(message)}, 200
		# Message id is not defined, return all messages
		else:
			# Get any filters passed as query parameters
			filters = g.validated_object.to_dict(sparse=False)
			messages = Message.query.filter_by(**filters)
			return {"messages": Message.schema(many=True).dump(messages)}, 200

	@auth.login_required
	@validate_with(Message.schema(partial=True))
	def post(self):
		"""
		Create a new message
		"""
		message = g.validated_object
		message.created_at = datetime.now()

		# Save message to db
		db.session.add(message)
		db.session.commit()

		# Respond to client
		return {"messages": Message.schema().dump(message)}, 201


	@auth.login_required
	@validate_with(Message.schema(partial=True))
	def put(self, message_id):
		# Update message
		message = Message.query.get(message_id)
		for k, v in request.json.items():
			setattr(message, k, v)
		db.session.add(message)
		db.session.commit()

		return {"messages": Message.schema().dump(message)}, 200


	@auth.login_required
	def delete(self, message_id):

		# Update message
		message = Message.query.get(message_id)
		db.session.delete(message)
		db.session.commit()

		return {}, 204

