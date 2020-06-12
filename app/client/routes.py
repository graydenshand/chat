from app.client import client
from flask import render_template

@client.route('/', defaults={'path': ''})
@client.route('/<path:path>')
def catch_all(path):
	return render_template("index.html")