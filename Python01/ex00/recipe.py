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
		if not all(isinstance(item, str) for item in ingredients):
			print("ingridients should be list of strings")
			return
		if not isinstance(description, str) and description is not None:
			print("description should be string")
			return
		if not isinstance(recipe_type, str):
			print("recipe_type should be string")
			return
		self.name = name
		if cooking_lvl > 5 or cooking_lvl < 1:
			print("Wrong cooking_lvl")
			return
		self.cooking_lvl = cooking_lvl
		if cooking_time < 0:
			print("Wrong cooking_time")
			return
		self.cooking_time = cooking_time
		self.ingredients = ingredients
		self.description = description
		if recipe_type not in ["starter", "lunch", "dinner"]:
			print("Wrong recipe_type")
			return
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
	def get_name(self):
		return self.name