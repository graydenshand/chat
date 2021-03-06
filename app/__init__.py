from flask import Flask
from flask_socketio import SocketIO
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from flask_migrate import Migrate
from flask_httpauth import HTTPBasicAuth, HTTPTokenAuth, MultiAuth

socketio = SocketIO(cors_allowed_origins="*")
api = Api()
basic_auth = HTTPBasicAuth()
token_auth = HTTPTokenAuth()
auth = MultiAuth(basic_auth, token_auth)
db = SQLAlchemy()
cors = CORS()
migrate = Migrate()


def create_app(debug=False, config=None):
	app = Flask(__name__)
	with app.app_context():
		# Load app config
		app.config.from_object(config)
		#app.token_serializer = Serializer(app.config['SECRET_KEY'], expires_in=3600)

		# Enable flask extensions
		socketio.init_app(app)
		api.init_app(app)
		db.init_app(app)
		cors.init_app(app)
		migrate.init_app(app, db)

		# Register Blueprints
		from .client import client as client_blueprint
		app.register_blueprint(client_blueprint)

		from .api.messages import messages as message_blueprint
		app.register_blueprint(message_blueprint)

		from .api.users import users as user_blueprint
		app.register_blueprint(user_blueprint)

		from .api.channels import channels as channel_blueprint
		app.register_blueprint(channel_blueprint)

		from .api.auth import auth as auth_blueprint
		app.register_blueprint(auth_blueprint)
		
		# Inject models into shell context
		from .api.models import User, Message, Channel
		@app.shell_context_processor
		def make_shell_context():
			return {
				"User": User, 
				"Message": Message, 
				"Channel": Channel,
				"Db": db
			}

	return app