import os

class Config(object):
	SECRET_KEY = 'g]fQU<XfE:5"%QkV'
	DEBUG = False
	TESTING = False
	DATABASE_URL = os.environ.get("DATABASE_URL")

class ProductionConfig(Config):
	pass

class DevelopmentConfig(Config):
	DEBUG = True
	DATABASE_URL = "postgres://localhost:5432/chat"

class TestingConfig(Config):
	TESTING = True
	DATABASE_URL = "postgres://localhost:5432/chat_test"