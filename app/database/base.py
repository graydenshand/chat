from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from flask import current_app, _app_ctx_stack
import os
import re


class Db():


	def __init__(self, app=None):
		self.app = app
		self.Base = declarative_base()
		if app is not None:
			self.init_app(app)

	def init_app(self, app):
		self.app = app
		self.make_session()

		@app.teardown_appcontext
		def shutdown_session(exception=None):
			print("tear down")
			self.session.close()

	def make_session(self):
		self.engine = create_engine(self.app.config['DATABASE_URL'], convert_unicode=True)
		self.session = scoped_session(
			sessionmaker(
				autocommit=False, 
				autoflush=False, 
				bind=self.engine
			)
		)
		self.Base.query = self.session.query_property()


	def create_all(self):
	    # import all modules here that might define models so that
	    # they will be registered properly on the metadata.  Otherwise
	    # you will have to import them first before calling init_db()
	    from .models.user import User
	    from .models.message import Message
	    self.Base.metadata.create_all(bind=self.engine)

	def drop_all(self):
		# Drops all tables from schema, useful for testing
		from .models.user import User
		from .models.message import Message
		self.Base.metadata.drop_all(bind=self.engine)

