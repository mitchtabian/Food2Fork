from django.urls import path

from recipe.api.views import (
	recipe_search,
	recipe_get,
)
app_name = 'recipe'

urlpatterns = [
 	path('search/', recipe_search, name="search"), 
 	path('get/', recipe_get, name="get"), 
]
