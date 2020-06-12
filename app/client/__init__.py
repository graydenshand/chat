from flask import Blueprint

client = Blueprint('client', __name__, static_folder='./app/dist/assets', template_folder='./app/dist')

# avoid circular import errors
from app.client import routes