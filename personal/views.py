from django.shortcuts import render
from django.conf import settings
from recipe.models import Recipe

import os

def home_screen_view(request):
	context = {}
	path = f"{settings.BASE_DIR}/recipe/api/"
	f = open(os.path.join(path, 'documentation.md'), 'r')
	file_content = f.read()
	f.close()
	context['documentation'] = file_content
	return render(request, "personal/home.html", context)

