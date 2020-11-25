from django.shortcuts import render


def recipe_view(request, *args, **kwargs):
	context = {}
	return render(request, "recipe/view.html", context)
