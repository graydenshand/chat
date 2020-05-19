from flask import Blueprint
from flask_restful import Api, Resource


users = Blueprint('users', __name__)
api = Api(users)

# avoid circular import errors
from app.users import events
from app.users import routes

api.add_resource(routes.Users, '/users.json', '/users/<int:user_id>.json')