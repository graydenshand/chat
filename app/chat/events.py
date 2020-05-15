from flask_socketio import emit, send, join_room, leave_room
from app import socketio

@socketio.on('message')
def handle_message(message):
	print(message)
	send(message)

@socketio.on('test')
def test(message):
	send(message)

@socketio.on('json')
def handle_json(json):
    send(json, json=True)

@socketio.on('myCustomEvent')
def handle_my_custom_event(message):
	print(message)
	emit('my response', message)
