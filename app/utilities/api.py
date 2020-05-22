"""
Common utility functions for api blueprints

"""

from functools import wraps
from flask_restful import abort
from flask import request, g
from marshmallow import ValidationError

def validate_with(schema):
	def validate_with_decorator(f):
		def wrapper(*args, **kwargs):
			# Validate data
			try:
				g.validated_object = schema.load(request.json)
			except ValidationError as err:
				abort(401, errors=err.messages)
			result = f(*args, **kwargs)
			return result
		return wrapper
	return validate_with_decorator