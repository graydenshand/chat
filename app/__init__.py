from flask import Flask
from flask_socketio import SocketIO
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from flask_migrate import Migrate
#from .database import Db

socketio = SocketIO(cors_allowed_origins="*")
api = Api()
db = SQLAlchemy()
cors = CORS()
migrate = Migrate()

def create_app(debug=False, config=None):
	app = Flask(__name__)

	# Load app config
	app.config.from_object(config)

	# Enable flask extensions
	socketio.init_app(app)
	api.init_app(app)
	db.init_app(app)
	cors.init_app(app)
	migrate.init_app(app, db)

	# Register Blueprints
	from app.js_client import js_client as js_client_blueprint
	app.register_blueprint(js_client_blueprint)

	from app.messages import messages as message_blueprint
	app.register_blueprint(message_blueprint)

	from app.users import users as user_blueprint
	app.register_blueprint(user_blueprint)

	from app.channels import channels as channel_blueprint
	app.register_blueprint(channel_blueprint)
	
	# Inject models into shell context
	from .models import User, Message, Channel
	@app.shell_context_processor
	def make_shell_context():
		return {
			"User": User, 
			"Message": Message, 
			"Channel": Channel,
			"Db": db
		}

	return app