from typing import ClassVar
from django.forms import ModelForm
from .models import *


class CookbookCreationForm(ModelForm):
    class Meta:
        model = Cookbook
        fields = ['name']


# class RecipeCreationForm(ModelForm):
#     class Meta:
#         model = 
#         fields = ['']
