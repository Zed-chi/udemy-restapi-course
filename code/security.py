from models.user import UserModel 

def auth(name, password):
	user = UserModel.find_by_username(name)
	if user and password ==  user.password:
		return user

def identity(payload):
	id = payload["identity"]
	return UserModel.find_by_id(id)
