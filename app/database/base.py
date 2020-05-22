from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from flask import current_app, _app_ctx_stack
import os
import re


class Db():
	Base = declarative_base()

	def __init__(self, app=None):
		self.app = app
		if app is not None:
			self.init_app(app)

	def init_app(self, app):
		self.app = app
		self.make_session()

		@app.teardown_appcontext
		def shutdown_session(exception=None):
			self.session.remove()

	def make_session(self):
		self.engine = create_engine(self.app.config['DATABASE_URL'], convert_unicode=True)
		self.session = scoped_session( sessionmaker(bind=self.engine) )
		self.Base.query = self.session.query_property()


	def create_all(self):
		# Build all tables from models
	    from .models.user import User
	    from .models.message import Message
	    self.Base.metadata.create_all(bind=self.engine)

	def drop_all(self):
		# Drops all tables from models, useful for testing
		from .models.user import User
		from .models.message import Message
		self.Base.metadata.drop_all(bind=self.engine)

