from django.contrib.auth import authenticate
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.settings import api_settings
from django.db.models import Q

from itertools import chain

from recipe.api.serializers import RecipeSerializer
from recipe.api.constants import ApiRecipeResponse
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

		pagination_class = api_settings.DEFAULT_PAGINATION_CLASS
		paginator = pagination_class()
		page = paginator.paginate_queryset(results, request)
		serializer = RecipeSerializer(page, many=True)
		return paginator.get_paginated_response(serializer.data)
	except Exception as e:
		return Response(str(e), status=status.HTTP_400_BAD_REQUEST)
	

	

@api_view(['GET', ])
@permission_classes((IsAuthenticated, ))
def recipe_get(request, *args, **kwargs):
	"""
	Get a single recipe given the id (pk).
	See [/recipe/api/documentation.md] for more information.
	"""
	rId = request.GET.get("id")

	if rId == None or rId == "":
		return Response(ApiRecipeResponse.INVALID_RECIPE_ID.value, status=status.HTTP_400_BAD_REQUEST)
	else:
		try:
			rId = int(rId)
		except ValueError:
			return Response(ApiRecipeResponse.INTEGER_RECIPE_ID.value, status=status.HTTP_400_BAD_REQUEST)
		try:
			recipe = Recipe.objects.get(pk=rId)
		except Recipe.DoesNotExist:
			return Response(ApiRecipeResponse.RECIPE_DOES_NOT_EXIST.value, status=status.HTTP_404_NOT_FOUND)
		return Response(RecipeSerializer(recipe).data)
	return Response(ApiRecipeResponse.UNKNOWN_ERROR.value, status=status.HTTP_400_BAD_REQUEST)



























