from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.forms import ModelForm, modelformset_factory
from django.utils.text import slugify

from .forms import CookbookCreationForm, RecipeCreationForm, IngredientForm
from .models import Cookbook, Ingredient, RecipeInfos


@login_required
def create_cookbook(request):
    if request.method == 'POST':
        form = CookbookCreationForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            Cookbook.objects.create(name=name, user=request.user)
            return redirect('home')
    else:
        form = CookbookCreationForm()

    return render(request, 'cookbook/cookbook-create.html', {'form': form})


@login_required
def create_recipe(request):
    IngredientFormSet = modelformset_factory(Ingredient, form=IngredientForm)
    data = {
        'form-TOTAL_FORMS': '3',
        'form-INITIAL_FORMS': '0',
        'form-MIN_NUM_FORMS': '3',
        'form-MAX_NUM_FORMS': '20',
    }

    if request.method == 'POST':
        recipe_form = RecipeCreationForm(request.POST)
        ingredient_formset = IngredientFormSet(request.POST)

        if recipe_form.is_valid() and ingredient_formset.is_valid():
            # Recipe
            recipe = recipe_form.save()
            # Recipe Infos
            creator = request.user
            owner = request.user
            slug = slugify(recipe.title)
            RecipeInfos.objects.create(creator=creator, owner=owner, slug=slug, recipe=recipe)
            # Ingredients
            ingredients = ingredient_formset.save(commit=False)
            for ingredient in ingredients:
                ingredient.recipe = recipe
                ingredient.save()

            return redirect('home')
    else:
        recipe_form = RecipeCreationForm()
        ingredient_formset = IngredientFormSet(data)

    context = {
        'recipe_form': recipe_form,
        'ingredient_formset': ingredient_formset,
    }
    return render(request, 'cookbook/recipe-create.html', context)