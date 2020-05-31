from app import db, socketio, basic_auth, token_auth
from app.auth import token_serializer
from app.models import User

def generate_token(user):
	token = token_serializer.dumps(User.schema(only=["id", "email"]).dump(user))
	print(f"*** TOKEN FOR {user.email}: {token}")
	return token

@token_auth.verify_token
def verify_token(token):
	print(token)
	try:
		data = token_serializer.loads(token)
	except:  # noqa: E722
		return False
	if 'id' in data:
		print(data)
		return User.query.get(data['id'])

@basic_auth.verify_password
def verify_password(email, password):
	return User.query.filter(User.email == email).first()

@basic_auth.error_handler
def auth_error(status):
	return "Unauthorized access", status