from django.urls import path

from recipe.views import (
	recipe_view
)

app_name = 'recipe'

urlpatterns = [
	path("recipe/<uuid>/", recipe_view, name='view'),
]

