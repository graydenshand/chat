from flask import Flask
from flask_socketio import SocketIO
from .database.base import db_session
from flask_restful import Api, Resource

socketio = SocketIO(cors_allowed_origins=["http://127.0.0.1:5000", "http://127.0.0.1:4200", "https://immense-meadow-61514.herokuapp.com"])
api = Api()

def create_app(debug=False):
	app = Flask(__name__)

	# Load app config
	app.config['SECRET_KEY'] = 'g]fQU<XfE:5"%QkV'

	# Enable flask extensions
	socketio.init_app(app)
	api.init_app(app)

	# Register Blueprints
	from app.js_client import js_client as js_client_blueprint
	from app.messages import messages as message_blueprint
	from app.users import users as user_blueprint
	app.register_blueprint(message_blueprint)
	app.register_blueprint(user_blueprint)
	app.register_blueprint(js_client_blueprint)
	

	return app