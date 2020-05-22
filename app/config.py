import os

class Config(object):
	SECRET_KEY = 'g]fQU<XfE:5"%QkV'
	DEBUG = False
	TESTING = False
	SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")

class ProductionConfig(Config):
	pass

class DevelopmentConfig(Config):
	DEBUG = True
	SQLALCHEMY_DATABASE_URI = "postgres://localhost:5432/chat"

class TestingConfig(Config):
	TESTING = True
	SQLALCHEMY_DATABASE_URI = "postgres://localhost:5432/chat_test"