from flask import Blueprint
from flask_restful import Api, Resource


messages = Blueprint('messages', __name__)
api = Api(messages)

# avoid circular import errors
from app.messages import events
from app.messages import routes

api.add_resource(routes.MessageResource, '/message.json', '/message/<int:message_id>.json')