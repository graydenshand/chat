from flask import request, g
from flask_restful import Resource, fields, abort
from ..models import Message
from app import db
from datetime import datetime
from marshmallow import ValidationError
from app.utilities.api import validate_with

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


	def get(self, message_id=None):
		"""
		Get one or many messages
		"""
		# Message id is defined, return the message with the specified id
		if message_id:
			message = Message.query.filter(Message.id == message_id).first()
			return {"messages": Message.schema().dump(message)}, 200
		# Message id is not defined, return all messages
		else:
			messages = Message.query.all()
			return {"messages": Message.schema(many=True).dump(messages)}, 200


	@validate_with(Message.schema())
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


	@validate_with(Message.schema(partial=True))
	def put(self, message_id):
		# Update message
		message = Message.query.filter(Message.id == message_id).first()
		for k, v in request.json.items():
			setattr(message, k, v)
		db.session.add(message)
		db.session.commit()

		return {"messages": Message.schema().dump(message)}, 200



	def delete(self, message_id):

		# Update message
		message = Message.query.filter(Message.id == message_id).first()
		db.session.delete(message)
		db.session.commit()

		return {}, 204

