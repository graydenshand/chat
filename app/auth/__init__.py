from flask import Blueprint, current_app
from flask_restful import Api, Resource
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer



auth = Blueprint('auth', __name__)
api = Api(auth)
token_serializer = Serializer(current_app.config['SECRET_KEY'], expires_in=3600)

# avoid circular import errors
from app.auth import routes

api.add_resource(routes.Auth, '/auth.json')