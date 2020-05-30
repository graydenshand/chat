"""
Common utility functions for api blueprints
"""

from functools import wraps
from flask_restful import abort
from flask import request, g
from marshmallow import ValidationError

def validate_with(schema):
	"""
	Validate JSON request using given schema, abort with 
	a 401 with error messages if schema validation fails.

	Usage:
		@validate_with(User.schema())
		def post():
			...
	"""
	def validate_with_decorator(f):
		def wrapper(*args, **kwargs):
			# Validate data
			try: 
				if request.is_json:
					print(request.json)
					# Store the validated object in the g context variable, enabling access from routes
					g.validated_object = schema.load(request.json)
				else:
					g.validated_object = schema.load(request.args.to_dict())
			except ValidationError as err:
				# Return an error if validation fails
				print(err.messages)
				abort(406, errors=[str(err.messages)])
			# run wrapped function
			result = f(*args, **kwargs)
			return result
		return wrapper
	return validate_with_decorator