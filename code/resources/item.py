from flask_restful import reqparse, Resource 
from flask_jwt import jwt_required
from models.item import ItemModel
import sqlite3


class Item(Resource):
	parser = reqparse.RequestParser()
	parser.add_argument("price", type=float, required=True)

	@jwt_required()
	def get(self, name):
		item = ItemModel.find_by_name(name)
		if item:
			return item.json()
		return {"message": "item not found"}, 404 
	
	
	def post(self, name):
		if ItemModel.find_by_name(name):
			return {"message": "item is already exists"}, 400
		data = Item.parser.parse_args()
		item = ItemModel(name, data["price"])
		try:
			item.insert()
		except:
			return {"message": "inserting error"}, 500
		return item.json(), 201

	def delete(self, name):
		conn = sqlite3.connect("data.db")
		cursor = conn.cursor()
		query = "delete from items where name=?"
		cursor.execute(query, (name,) )
		conn.commit()
		conn.close()
		return {"message": "items deleted"}

	def put(self, name):
		data = Item.parser.parse_args()
		item = ItemModel.find_by_name(name)
		upd_item = ItemModel(name, data["price"])
		if item is None:
			try:
				upd_item.insert()
			except:
				return {"message": "insertion error"}, 500
		else:
			try:
				upd_item.update()
			except:
				return {"message": "update error"}, 500
		return upd_item.json()


class ItemList(Resource):
	def get(self):
		conn = sqlite3.connect("data.db")
		cursor = conn.cursor()
		query = "select * from items"
		result = cursor.execute(query)
		items = [{"name":row[0], "price":row[1]} for row in result]
		conn.close()
		return {"items": items}