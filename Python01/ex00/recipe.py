class Recipe:
	def __init__(self, name:str, cooking_lvl:int, cooking_time:int, ingredients:list, description:str, recipe_type:str):
		if not isinstance(name, str):
			print("name should be string")
			return
		if not isinstance(cooking_lvl, int):
			print("cooking_lvl should be int")
			return
		if not isinstance(cooking_time, int):
			print("cooking_time should be int")
			return
		if not isinstance(ingridients, list):
			print("ingridients should be list")
			return
		if not isinstance(description, str) and not isinstance(description, None):
			print("description should be string")
			return
		if not isinstance(recipe_type, str):
			print("recipe_type should be string")
			return
		self.name = name
		self.cooking_lvl = cooking_lvl
		self.cooking_time = cooking_time
		self.ingredients = ingredients
		self.description = description
		self.recipe_type = recipe_type