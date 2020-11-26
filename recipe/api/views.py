from django.contrib.auth import authenticate
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from django.db.models import Q

from itertools import chain

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
	data = []
	try:
		queries = q.split(" ")
		results = []
		for query in queries:
			result = Recipe.objects.filter(
				Q(title__icontains=query) 
				| Q(publisher__username__icontains=query)
				| Q(description__icontains=query)
				| Q(ingredients__icontains=query)
			)
			results.append(result)

		# Flatten the list of querysets into a single list
		results = list(chain.from_iterable(results))

		# Ensure the list items are unique
		results = list(set(results))

		# Serialize
		for recipe in results:
			data.append(RecipeSerializer(recipe).data)
		return Response(data)
	except Exception as e:
		return Response(str(e), status=status.HTTP_400_BAD_REQUEST)
	

	




























