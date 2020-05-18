from flask import Flask
from flask_socketio import SocketIO
from .database.base import db_session
from flask_restful import Api, Resource

socketio = SocketIO(cors_allowed_origins=["http://127.0.0.1:5000", "http://127.0.0.1:4200", "https://immense-meadow-61514.herokuapp.com"])
api = Api()

def create_app(debug=False):
	app = Flask(__name__)
	app.config['SECRET_KEY'] = 'g]fQU<XfE:5"%QkV'

	socketio.init_app(app)
	api.init_app(app)

	from app.messages import messages as message_blueprint
	from app.js_client import js_client as js_client_blueprint
	app.register_blueprint(message_blueprint)
	app.register_blueprint(js_client_blueprint)

	
	return app