from django.contrib import admin
from recipe.models import Recipe



class RecipeAdmin(admin.ModelAdmin):
	list_display = ('title','publisher','date_added', 'date_updated', 'rating','id')
	search_fields = ('title','publisher__username', 'publisher__email', 'id')
	readonly_fields=('id', 'date_added', )

	filter_horizontal = ()
	list_filter = ()
	fieldsets = ()


admin.site.register(Recipe, RecipeAdmin)