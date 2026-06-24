import sys

def print_all_recipes(cookbook):
	if not cookbook:
		print("Cookbook is empty")
		return
	print("\nPrinting all recipes:")
	for item in cookbook:
		print_recipe(cookbook, item)

def print_recipe(cookbook, name):
	if not name in cookbook:
		print("no entry in cookbook under", name)
		return
	item = cookbook[name]
	print(f"Recipe for {name}:")
	print(f"	Ingredients: {item['ingredients']}.")
	print(f"	To be eaten for {item['meal']}.")
	print(f"	Takes {item['prep_time']} minutes of cooking.")

def delete_recipe(cookbook, name):
	try:
		cookbook.pop(name)
	except KeyError:
		print("no such entry in cookbook, nothing deleted")
		return

def add_recipe(cookbook):
	print("Please enter the name of the recipe:")
	name = input(">>")
	print("The ingredients:")
	ingredients = input(">>").split()
	print("The meal:")
	meal = input(">>")
	print("The preparaton time:")
	prep_time = input(">>")
	try:
		prep_time = int(prep_time)
	except ValueError:
		print("Prep_time not a valid int")
		return 
	if (prep_time < 0):
		print("Prep_time not a valid int")
		return 
	cookbook[name] = {"ingredients": ingredients, "meal": meal, "prep_time": prep_time}

def main():
	cookbook = {
	"Sandwich" : {"ingredients": ["ham", "bread", "cheese", "tomatoes"], "meal": "lunch", "prep_time": 10},
	"Cake" : {"ingredients": ["flour", "sugar", "eggs"], "meal": "dessert", "prep_time": 60},
	"Salad" : {"ingredients": ["avocado", "arugula", "tomatoes", "spinach"], "meal": "lunch", "prep_time": 15}
	}
	print("Welcome to my cookbook!")
	while True:
		print("\nPlease select the number of the option:")
		print("1. Add a recipe\n2. Delete a recipe\n3. Print a recipe\n4. Print the cookbook\n5. quit")
		option = input(">>")
		try:
			option = int(option)
		except ValueError:
			print("\nNo such option, try again")
			continue
		if option > 5 or option < 1:
			print("\nNo such option, try again")
			continue
		if option == 1:
			add_recipe(cookbook)
		if option == 2:
			name = input("Which recipe? (Enter a name)\n>>")
			delete_recipe(cookbook, name)
		if option == 3:
			name2 = input("Which recipe? (Enter a name)\n>>")
			print_recipe(cookbook, name2)
		if option == 4:
			print_all_recipes(cookbook)
		if option == 5:
			break


if __name__ == "__main__":
    main()