import os
import tempfile

import pytest

from app import create_app
from app.database.base import Db
from app.config import TestingConfig

app = create_app(config=TestingConfig)
db = Db(app)

@pytest.fixture(scope="module")
def client():
	"""Set up a test fixture with flask client"""
	app.config['TESTING'] = True
	with app.test_client() as client:
		with app.app_context():
			# Construct a new, empty database schema
			db.create_all()
		yield client

	# Close Db session and drop all tables
	db.session.close()
	db.drop_all()

def test_messages(client):
    """Start with a blank database."""

    rv = client.get('/messages.json')
    json_data = rv.get_json()
    assert 'messages' in json_data.keys()
    assert len(json_data['messages']) == 0