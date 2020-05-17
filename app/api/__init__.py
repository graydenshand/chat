from flask import Blueprint

api = Blueprint('api', __name__)

# avoid circular import errors
from app.api import events