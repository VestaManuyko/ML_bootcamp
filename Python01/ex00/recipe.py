class Recipe:
	def __init__(self, name:str, cooking_lvl:int, cooking_time:int, ingredients:list, recipe_type:str, description:str = None):
		if not isinstance(name, str):
			print("name should be string")
			return
		if not isinstance(cooking_lvl, int):
			print("cooking_lvl should be int")
			return
		if not isinstance(cooking_time, int):
			print("cooking_time should be int")
			return
		if not isinstance(ingredients, list):
			print("ingridients should be list")
			return
		if not isinstance(description, str) and description is not None:
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
	def __str__(self):
		"""Returns the string to print with the recipe’s info"""
		txt = "Name:" + self.name + "\nCooking_lvl:" + str(self.cooking_lvl)
		txt += "\nCooking_time:" + str(self.cooking_time)
		txt += "\nIngredients:"
		for item in self.ingredients:
			txt += item
		if isinstance(self.description, str):
			txt += "\nDescription:" + self.description
		txt += "\nRecipe_type:" + self.recipe_type
		return txt