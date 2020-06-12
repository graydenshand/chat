from flask_restful import Resource, fields
from flask import g, request
from ..models import Channel
from app import db, socketio, auth
from datetime import datetime
from app.api.utilities.api import validate_with

class Channels(Resource):
	"""
	Channel resource
	
	GET /channels.json
		* Returns list of channels 
		* [params] ?name=channelName get by name
	GET /channels/<channel_id>.json
		* Returns a single channel 
	POST /channels.json
		* Creates a new channel
	PUT /channels/<channel_id>.json
		* Updates a channel
	DELETE /channels/<channel_id>.json
		* Deletes a channel
	"""
	@auth.login_required
	@validate_with(Channel.schema(only=["name"], partial=True))
	def get(self, channel_id=None):
		"""
		Get one or many messages
		"""
		if channel_id:
			# Channel id is defined
			## return the channel with the specified id
			channel = Channel.query.get(channel_id)
			return {"channels": Channel.schema().dump(channel)}, 200
		else:
			if request.args.get("name"):
				# Filter by name
				channels = Channel.query.filter(Channel.name == g.validated_object.name).all()
				return {"channels": Channel.schema(many=True).dump(channels)}, 200
			else:
				# return all results as list
				channels = Channel.query.all()
				return {"channels": Channel.schema(many=True).dump(channels)}, 200

	@auth.login_required
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

	@auth.login_required
	@validate_with(Channel.schema())
	def put(self, channel_id):

		# Update channel
		channel = Channel.query.get(channel_id)
		for k, v in request.json.items():
			setattr(channel, k, v)
		db.session.add(channel)
		db.session.commit()

		return {"channels": Channel.schema().dump(channel)}, 200


	@auth.login_required
	def delete(self, channel_id):

		# Update channel
		channel = Channel.query.get(channel_id)
		db.session.delete(channel)
		db.session.commit()

		return {}, 204
