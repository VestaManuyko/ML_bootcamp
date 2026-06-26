import datetime

class Book:
	def __init__(self, name:str, last_update:datetime, creation_date:datetime, recipes_list:dict):
		if not isinstance(name, str)
			print("name should be string")
			return
		if not isinstance(last_update, datetime)
			print("last_update should be datetime")
			return
		if not isinstance(creation_date, datetime)
			print("creation_date should be datetime")
			return
		if not isinstance(recipes_list, dict)
			print("recipes_list should be list")
			return
		self.name = name
		self.last_update = last_update
		self.creation_date = creation_date
		self.recipes_list = recipes_list