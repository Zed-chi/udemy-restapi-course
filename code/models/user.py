from flask_restful import reqparse, Resource 
from flask_jwt import jwt_required
import sqlite3


class UserModel():
	def __init__(self, _id, name, password):
		self.id = _id
		self.name = name
		self.password = password
	
	@classmethod
	def find_by_username(cls, name):
		con = sqlite3.connect("data.db")
		cursor = con.cursor()

		query = "select * from users where username=?"
		result = cursor.execute(query, (name,))
		row = result.fetchone()
		if row:
			user = cls(*row)
		else:
			user = None
		con.close()
		return user

	@classmethod
	def find_by_id(cls, _id):
		con = sqlite3.connect("data.db")
		cursor = con.cursor()

		query = "select * from users where id=?"
		result = cursor.execute(query, (_id,))
		row = result.fetchone()
		if row:
			user = cls(*row)
		else:
			user = None
		con.close()
		return user		
	