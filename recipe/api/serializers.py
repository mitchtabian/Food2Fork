from rest_framework import serializers

from recipe.models import Recipe

class RecipeSerializer(serializers.ModelSerializer):

	publisher = serializers.SerializerMethodField('get_username_from_publisher')
	featured_image 	 = serializers.SerializerMethodField('get_featured_image')

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

	def get_featured_image(self, recipe):
		return recipe.get_featured_image_url()










