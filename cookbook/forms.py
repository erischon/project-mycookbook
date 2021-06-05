# from typing import ClassVar
from django.forms import ModelForm, modelformset_factory
from django.forms.widgets import TextInput, Textarea

from .models import Cookbook, Recipe, Ingredient, Instruction, TagType, Tag


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
        widgets = {
            'title': TextInput(attrs={'placeholder': 'Nom de la recette', 'class': 'bg-gray-50 p-3 mb-4 w-full sm:w-1/2 shadow-md border-0 rounded'}),
            'description': Textarea(attrs={'placeholder': 'Une description', 'class': 'bg-gray-100 p-3 mb-4 w-full sm:w-1/2 shadow-md rounded', 'rows': 3}),
            'guest': TextInput(attrs={'placeholder': 'pour combien de personne ?', 'class': 'bg-gray-50 p-3 mb-4 w-full sm:w-1/2 shadow-md border-0 rounded'}),
            'prep_time': TextInput(attrs={'placeholder': 'Temps de préparation (00:00:00)', 'class': 'bg-gray-50 p-3 mb-4 w-full sm:w-1/2 shadow-md border-0 rounded'}),
            'cook_time': TextInput(attrs={'placeholder': 'Temps de cuisson (00:00:00)', 'class': 'bg-gray-50 p-3 mb-4 w-full sm:w-1/2 shadow-md border-0 rounded'}),
            'source': TextInput(attrs={'placeholder': 'Source', 'class': 'bg-gray-100 p-3 mb-4 w-full sm:w-1/2 shadow-md border-0 rounded'}),
        }


class IngredientForm(ModelForm):
    class Meta:
        model = Ingredient
        fields = ['name', 'measure', 'quantity']
        labels = {
            'name': 'Ingédient : ',
            'measure': 'Mesure : ',
            'quantity': 'Quantité : ',
        }
        widgets = {
            'name': TextInput(attrs={'placeholder': 'Ingrédient', 'class': 'bg-gray-50 p-3 mb-2 w-full sm:w-1/2 shadow-md border-0 rounded'}),
            'quantity': TextInput(attrs={'placeholder': 'Quantité', 'class': 'bg-gray-50 p-3 mb-2 w-40 sm:w-1/2 shadow-md border-0 rounded'}),
            'measure': TextInput(attrs={'placeholder': 'Mesure', 'class': 'bg-gray-50 p-3 mb-2 w-40 sm:w-1/2 shadow-md border-0 rounded'}),
        }


class InstructionForm(ModelForm):
    class Meta:
        model = Instruction
        fields = ['step', 'instruction']
        labels = {
            'step': 'Etape : ',
            'instruction': 'Instruction : ',
        }
        widgets = {
            'instruction': Textarea(attrs={'cols': 20, 'rows': 3}),
        }


class TagForm(ModelForm):
    class Meta:
        model = Tag
        fields = ['name', 'tagtype']
        labels = {
            'name': 'Tag : ',
            'tagtype': 'Catégorie : ',
        }
