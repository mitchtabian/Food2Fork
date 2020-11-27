from recipe.models import Recipe


def fix():
	for recipe in Recipe.objects.all():
		ingredients = []
		for i in recipe.ingredients:
			ingredients.append(i)
			# print(str(i))
		recipe.ingredient_list = ingredients
		recipe.save()



def fix2():
	for recipe in Recipe.objects.all():
		ingredients = []
		for i in recipe.ingredient_list:
			ingredients.append(i)
			# print(str(i))
		recipe.ingredients = ingredients
		recipe.save() 






