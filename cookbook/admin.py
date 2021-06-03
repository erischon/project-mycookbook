from django.contrib import admin
from .models import Cookbook, Recipe, RecipeInfos, Ingredient


class RecipeInfosAdmin(admin.ModelAdmin):
    readonly_fields = ('creation_date', 'modification_date',)

admin.site.register(Cookbook)
admin.site.register(Recipe)
admin.site.register(RecipeInfos, RecipeInfosAdmin)
admin.site.register(Ingredient)
