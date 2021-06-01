from typing import ClassVar
from django.forms import ModelForm
from .models import Cookbook, Recipe, Ingredient, Quantity


class CookbookCreationForm(ModelForm):
    class Meta:
        model = Cookbook
        fields = ['name']


class RecipeCreationForm(ModelForm):
    class Meta:
        model = Recipe
        fields = ['title', 'description', 'guest', 'prep_time', 'cook_time', 'source']
        labels = {
            'title': 'Nom de la recette ',
            'description': 'Une description ',
            'guest': 'Pour combien de personne ',
            'prep_time': 'Temps de préparation ',
            'cook_time': 'Temps de cuisson ',
            'source': 'Source de la recette'
        }


class IngredientForm(ModelForm):
    class Meta:
        model = Ingredient
        fields = ['name']
        labels = {
            'name': 'Nom de l\'ingredient ',
        }

class QuantityForm(ModelForm):
    class Meta:
        model = Quantity
        fields = ['measure', 'quantity']
        labels = {
            'measure': 'le type de mesure ',
            'quantity': 'la quantité'
        }