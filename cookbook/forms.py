# from typing import ClassVar
from django.forms import ModelForm, modelformset_factory
from django.forms.widgets import Select, TextInput, Textarea

from .models import Cookbook, Recipe, Ingredient, Instruction, TagType, Tag


class CookbookCreationForm(ModelForm):
    """ Cookbook creation Form (no longer used). """
    class Meta:
        model = Cookbook
        fields = ['name']


class RecipeCreationForm(ModelForm):
    """ Recipe Form. """
    class Meta:
        model = Recipe
        fields = ['title', 'description', 'recipe_type', 'guest', 'prep_time', 'cook_time', 'source']
        labels = {
            'title': 'Nom de la recette ',
            'description': 'Une description ',
            'recipe_type': 'Type de recette ',
            'guest': 'Pour combien de personne ',
            'prep_time': 'Temps de préparation ',
            'cook_time': 'Temps de cuisson ',
            'source': 'Source de la recette'
        }
        widgets = {
            'title': TextInput(attrs={'placeholder': 'Nom de la recette', 'class': 'bg-gray-50 p-3 mb-4 w-full sm:w-1/2 shadow-md border-0 rounded'}),
            'description': Textarea(attrs={'placeholder': 'Une description', 'class': 'bg-gray-50 p-3 mb-4 w-full sm:w-1/2 shadow-md rounded', 'rows': 3}),
            'recipe_type': Select(attrs={'class': 'bg-gray-50 p-3 mb-4 w-full sm:w-1/3 shadow-md border-0 rounded'}),
            'guest': TextInput(attrs={'placeholder': 'Pour combien de personne ?', 'class': 'bg-gray-50 p-3 mb-4 w-full sm:w-1/2 shadow-md border-0 rounded'}),
            'prep_time': TextInput(attrs={'placeholder': 'Temps de préparation (00:00:00)', 'class': 'bg-gray-50 p-3 mb-4 w-full sm:w-1/2 shadow-md border-0 rounded'}),
            'cook_time': TextInput(attrs={'placeholder': 'Temps de cuisson (00:00:00)', 'class': 'bg-gray-50 p-3 mb-4 w-full sm:w-1/2 shadow-md border-0 rounded'}),
            'source': TextInput(attrs={'placeholder': 'Source', 'class': 'bg-gray-50 p-3 mb-4 w-full sm:w-1/2 shadow-md border-0 rounded'}),
        }


class IngredientForm(ModelForm):
    """ Ingredient Form. """
    class Meta:
        model = Ingredient
        fields = ['name', 'measure', 'quantity']
        labels = {
            'name': 'Ingédient ',
            'measure': 'Mesure ',
            'quantity': 'Quantité ',
        }
        widgets = {
            'name': TextInput(attrs={'placeholder': 'Ingrédient', 'class': 'bg-gray-50 p-3 mb-2 w-full sm:w-full shadow-md border-0 rounded'}),
            'quantity': TextInput(attrs={'placeholder': 'Quantité', 'class': 'bg-gray-50 p-3 mb-2 w-40 sm:w-full shadow-md border-0 rounded'}),
            'measure': TextInput(attrs={'placeholder': 'Mesure (kg, pincée, ...)', 'class': 'bg-gray-50 p-3 mb-2 w-40 sm:w-full shadow-md border-0 rounded'}),
        }


class InstructionForm(ModelForm):
    """ Instruction Form. """
    class Meta:
        model = Instruction
        fields = ['step', 'instruction']
        labels = {
            'step': 'Etape ',
            'instruction': 'Instruction ',
        }
        widgets = {
            'step': TextInput(attrs={'placeholder': 'Etape n°', 'class': 'bg-gray-50 p-3 mb-2 w-40 sm:w-full shadow-md border-0 rounded'}),
            'instruction': Textarea(attrs={'placeholder': 'Instructions...', 'class': 'bg-gray-50 p-3 mb-4 w-full shadow-md rounded', 'rows': 3}),
        }


class TagForm(ModelForm):
    """ Tag Form. """
    class Meta:
        model = Tag
        fields = ['tagtype', 'name']
        labels = {
            'name': 'Tag ',
            'tagtype': 'Catégorie ',
        }
        widgets = {
            'name': TextInput(attrs={'placeholder': 'Nom du tag', 'class': 'bg-gray-50 p-3 mb-2 w-full sm:w-full shadow-md border-0 rounded'}),
        }
