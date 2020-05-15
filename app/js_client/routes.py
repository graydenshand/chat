from app.js_client import js_client
from flask import render_template

@js_client.route('/', defaults={'path': ''})
@js_client.route('/<path:path>')
def catch_all(path):
	return render_template("index.html")