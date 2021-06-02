from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required


from .forms import CookbookCreationForm, IngredientFormSet, RecipeCreationForm, IngredientFormSet
from .models import Cookbook, Ingredient


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
    if request.method == 'POST':
        recipe_form = RecipeCreationForm(request.POST)
        ingredient_formset = IngredientFormSet(request.POST)

        if recipe_form.is_valid():
            recipe = recipe_form.save()
            ingredients = ingredient_formset.save(commit=False)
            for ingredient in ingredients:
                ingredient.recipe = recipe
                ingredient.save()
            return redirect('home')
    else:
        form = RecipeCreationForm()

    recipe_form = RecipeCreationForm()
    ingredient_formset = IngredientFormSet()

    context = {
        'recipe_form': recipe_form,
        'ingredient_formset': ingredient_formset,
    }
    return render(request, 'cookbook/recipe-create.html', context)