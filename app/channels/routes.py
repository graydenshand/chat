from flask_restful import Resource, fields
from flask import g
from ..models import Channel
from app import db
from datetime import datetime
from app.utilities.api import validate_with
from app import socketio

class Channels(Resource):
	"""
	Channel resource
	
	GET /channels.json
		* Returns list of channels 
	GET /channels/<channel_id>.json
		* Returns a single channel 
	POST /channels.json
		* Creates a new channel
	PUT /channels/<channel_id>.json
		* Updates a channel
	DELETE /channels/<channel_id>.json
		* Deletes a channel
	"""
	
	def get(self, channel_id=None):
		"""
		Get one or many messages
		"""
		# Channel id is defined, return the channel with the specified id
		if channel_id:
			channel = Channel.query.filter(Channel.id == channel_id).first()
			return {"channels": Channel.schema().dump(channel)}, 200
		# Channel id is not defined, return all channels
		else:
			socketio.emit("message", "Get Channels")
			channels = Channel.query.all()
			return {"channels": Channel.schema(many=True).dump(channels)}, 200

	@validate_with(Channel.schema())
	def post(self):
		"""
		Create a new channel
		"""
		# Create channel
		channel = g.validated_object
		channel.created_at = datetime.now()

		# Save channel to db
		db.session.add(channel)
		db.session.commit()

		# Respond to client
		return {"channels": Channel.schema().dump(channel)}, 201


	@validate_with(Channel.schema())
	def put(self, channel_id):

		# Update channel
		channel = Channel.query.filter(Channel.id == channel_id).first()
		for k, v in request.json.items():
			setattr(channel, k, v)
		db.session.add(channel)
		db.session.commit()

		return {"channels": Channel.schema().dump(channel)}, 200



	def delete(self, channel_id):

		# Update channel
		channel = Channel.query.filter(Channel.id == channel_id).first()
		db.session.delete(channel)
		db.session.commit()

		return {}, 204
