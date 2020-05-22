from flask import Flask
from flask_socketio import SocketIO
from flask_restful import Api, Resource
from flask_sqlalchemy import SQLAlchemy
from .database import Db

socketio = SocketIO(cors_allowed_origins=["http://127.0.0.1:5000", "http://127.0.0.1:4200", "https://immense-meadow-61514.herokuapp.com"])
api = Api()
db = Db()

def create_app(debug=False, config=None):
	app = Flask(__name__)

	# Load app config
	app.config.from_object(config)

	# Enable flask extensions
	socketio.init_app(app)
	api.init_app(app)
	db.init_app(app)

	# Register Blueprints
	from app.js_client import js_client as js_client_blueprint
	from app.messages import messages as message_blueprint
	from app.users import users as user_blueprint
	app.register_blueprint(message_blueprint)
	app.register_blueprint(user_blueprint)
	app.register_blueprint(js_client_blueprint)
	
	# Inject models into shell context
	from .database.models import User, Message
	@app.shell_context_processor
	def make_shell_context():
		return {
			"User": User, 
			"Message": Message, 
			"Db": db
		}

	return app