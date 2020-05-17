#!/bin/env python
from app import create_app, socketio
from app.database.models import *
from app.database.base import db_session
import os

app = create_app(debug=True)

@app.teardown_appcontext
def shutdown_session(exception=None):
	db_session.remove()

@app.shell_context_processor
def make_shell_context():
	return {
		"User": User, 
		"Message": Message, 
		"db_session": db_session
	}

if __name__ =='__main__':
	socketio.run(app, host='0.0.0.0', port=os.environ.get('PORT'))