from django.shortcuts import render

from recipe.models import Recipe

def home_screen_view(request):
	context = {}
	recipes = Recipe.objects.all()
	context['recipes'] = recipes
	return render(request, "personal/home.html", context)

