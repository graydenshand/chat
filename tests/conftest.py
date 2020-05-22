import pytest
from app import create_app, db
from app.config import TestingConfig

app = create_app(config=TestingConfig)

@pytest.fixture(scope="session")
def client():
	"""Set up a test fixture with flask client"""
	app.config['TESTING'] = True
	with app.test_client() as client:
		with app.app_context():
			# Construct a new, empty database schema
			db.create_all()
		yield client

		# Close Db session and drop all tables
		db.session.remove()
		db.drop_all()