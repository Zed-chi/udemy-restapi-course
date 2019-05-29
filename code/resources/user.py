from flask_restful import Resource, reqparse
from models.user import UserModel
import sqlite3	


class UserRegister(Resource):
	parser = reqparse.RequestParser()
	parser.add_argument("username", type=str, required=True)
	parser.add_argument("password", type=str, required=True)

	def post(self):
		data = UserRegister.parser.parse_args()
		if UserModel.find_by_username(data["username"]):
			return {"message": "user exists"}, 400
		con = sqlite3.connect("data.db")
		cursor = con.cursor()
		query = "insert into users values (null, ?, ?)"
		cursor.execute(query, (data["username"], data["password"]))
		con.commit()
		con.close()
		return {"message": "user registered successfully"}, 201