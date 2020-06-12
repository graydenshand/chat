from flask import Blueprint
from flask_restful import Api, Resource


channels = Blueprint('channels', __name__)
api = Api(channels)

# avoid circular import errors
from app.api.channels import events
from app.api.channels import routes

api.add_resource(routes.Channels, '/channels.json', '/channels/<int:channel_id>.json')