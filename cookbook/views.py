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
        # recipe_form = RecipeCreationForm(request.POST)
        ingredient_formset = IngredientFormSet(request.POST)

        if ingredient_formset.is_valid():
        # if recipe_form.is_valid() and ingredient_formset.is_valid():
            # recipe = recipe_form.save()
            # ingredient = ingredient_formset
            # name = ingredient.cleaned_data['name']
            # quantity = ingredient.cleaned_data['quantity']
            # measure = ingredient.cleaned_data['measure']
            # Ingredient.objects.create(name=name, quantity=quantity, measure=measure, recipe=recipe)
            return redirect('home')
    else:
        form = RecipeCreationForm()

    # recipe_form = RecipeCreationForm(request.POST)
    ingredient_formset = IngredientFormSet(request.POST)

    context = {
        # 'recipe_form': recipe_form,
        'ingredient_formset': ingredient_formset,
    }
    return render(request, 'cookbook/recipe-create.html', context)