from user import User 

users = [
	User(1,"bob","qwe")
]

user_name_mapping = { u.name: u for u in users }
user_id_mapping = { u.id: u for u in users }

def auth(name, password):
	user = user_name_mapping.get(name, None)
	if user and password ==  user.password:
		return user

def identity(payload):
	id = payload["identity"]
	return user_id_mapping.get(id, None)
