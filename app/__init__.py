from flask import Flask
from flask_socketio import SocketIO

socketio = SocketIO(cors_allowed_origins=["http://127.0.0.1:5000", "http://127.0.0.1:4200"])


def create_app(debug=False):
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'g]fQU<XfE:5"%QkV'

    socketio.init_app(app)

    from app.chat import chat as chat_blueprint
    from app.js_client import js_client as js_client_blueprint
    app.register_blueprint(chat_blueprint)
    app.register_blueprint(js_client_blueprint)
    
    return app