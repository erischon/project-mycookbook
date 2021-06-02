from django.contrib import admin
from .models import Cookbook, Recipe, Ingredient


admin.site.register(Cookbook)
admin.site.register(Recipe)
admin.site.register(Ingredient)
