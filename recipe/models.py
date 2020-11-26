from django.db import models
from django.contrib.postgres.fields import JSONField
from django.conf import settings
from django.core.validators import MaxValueValidator, MinValueValidator
import uuid


def default_featured_image_filepath(self, filename):
	return f'featured_images/{str(self.pk)}/featured_image.png'

def default_featured_image():
	return "food2fork/default_featured_image.png"

class Recipe(models.Model):

	# title of a recipe
	title					= models.CharField(max_length=250, null=False, blank=False)

	# Thumbnail image
	featured_image			= models.ImageField(max_length=255, upload_to=default_featured_image_filepath, default=default_featured_image)

	# Other images of the recipe
	#images 					= models.??

	# Rating from 1-100
	rating					= models.IntegerField(default=1, validators=[MaxValueValidator(100), MinValueValidator(1)])

	# Who published this recipe
	publisher 				= models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,)

	# Link to where this recipe came from 
	source_url 				= models.URLField(max_length=300, blank=True, null=True,)

	# Description of the recipe
	description 			= models.CharField(max_length=500, blank=False, null=False)

	# Instructions for cooking the recipe
	cooking_instructions 	= models.TextField(blank=True, null=True)

	# List of ingredients
	"""
	{
		"Butter": "2 tablespoons",
		"Milk": "250ml",
		...
	}
	"""
	ingredients 			= JSONField()

	# Date the recipe was field published
	date_added 				= models.DateTimeField(auto_now_add=True)

	# When the recipe was updated
	date_updated			= models.DateTimeField()

	def __str__(self):
		return self.title

	def get_featured_image_url(self):
		return f"{settings.BASE_URL}{self.featured_image.url}"








