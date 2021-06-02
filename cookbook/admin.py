from django.contrib import admin
from .models import Cookbook, Recipe, RecipeInfos, Ingredient


admin.site.register(Cookbook)
admin.site.register(Recipe)
admin.site.register(RecipeInfos)
admin.site.register(Ingredient)
