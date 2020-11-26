from rest_framework import serializers

from datetime import datetime

from recipe.models import Recipe

class RecipeSerializer(serializers.ModelSerializer):

	publisher = serializers.SerializerMethodField('get_username_from_publisher')
	featured_image 	 = serializers.SerializerMethodField('get_featured_image')
	date_added = serializers.SerializerMethodField('humanize_date_added')
	date_updated = serializers.SerializerMethodField('humanize_date_updated')

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
		request = self.context.get('request')
		url = recipe.featured_image.url
		if "?" in url:
			url = recipe.featured_image.url[:recipe.featured_image.url.rfind("?")]
		return request.build_absolute_uri(url)

	def humanize_date_added(self, recipe):
		return recipe.date_added.strftime("%Y-%m-%d")

	def humanize_date_updated(self, recipe):
		return recipe.date_updated.strftime("%Y-%m-%d")









