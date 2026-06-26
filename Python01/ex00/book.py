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
	def get_recipe_by_name(self, name):
		"""Prints a recipe with the name \texttt{name} and returns the instance"""

	def get_recipes_by_types(self, recipe_type):
		"""Gets all recipes names for a given recipe_type """

	def add_recipe(self, recipe):
		"""Adds a recipe to the book and updates last_update"""
	if not isinstance(recipe, Recipe)
		print("not a recipe, try again")
		return
	self.recipes_list[recipe.get_name()] = recipe