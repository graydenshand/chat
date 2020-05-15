from flask import Blueprint

js_client = Blueprint('js_client', __name__, static_folder='./app/dist/assets', template_folder='./app/dist')

# avoid circular import errors
from app.js_client import routes