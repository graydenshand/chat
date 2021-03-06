from flask import Blueprint
from flask_restful import Api, Resource


messages = Blueprint('messages', __name__)
api = Api(messages)

# avoid circular import errors
from app.api.messages import events
from app.api.messages import routes

api.add_resource(routes.Messages, '/messages.json', '/messages/<int:message_id>.json')