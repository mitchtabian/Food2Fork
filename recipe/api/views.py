from django.contrib.auth import authenticate
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated

from recipe.api.serializers import RecipeSerializer
from recipe.models import Recipe


@api_view(['GET', ])
@permission_classes((IsAuthenticated, ))
def recipe_search(request, *args, **kwargs):
	"""
	Search for recipes.
	See [/recipe/api/documentation.md] for more information.
	"""
	q = request.GET.get("query")
	print(f"Q: {q}")
	data = []
	try:
		recipes = Recipe.objects.filter(
			title__icontains=str(q),
		)
		# .filter(
		# 	publisher__username__icontains=q,
		# ).filter(
		# 	description__icontains=q, 
		# )
		# .filter(
		# 	ingredients__icontains=q,
		# )
		for recipe in recipes:
			data.append(RecipeSerializer(recipe).data)
		return Response(data)
	except Exception as e:
		return Response(str(e), status=status.HTTP_400_BAD_REQUEST)
	

	




























