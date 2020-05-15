from flask import Blueprint

chat = Blueprint('chat', __name__)

# avoid circular import errors
from app.chat import events