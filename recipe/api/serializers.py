from rest_framework import serializers

from recipe.models import Recipe

class RecipeSerializer(serializers.ModelSerializer):

	publisher = serializers.SerializerMethodField('get_username_from_publisher')

	class Meta:
		model = Recipe
		fields = [
			'pk', 
			'title', 
			'publisher',
			'featured_image', 
			'rating', 
			'source_url', 
			'description', 
			'cooking_instructions',
			'ingredients',
			'date_added',
			'date_updated',
		]

	def get_username_from_publisher(self, recipe):
		return recipe.publisher.username












