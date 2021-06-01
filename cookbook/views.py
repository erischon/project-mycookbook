from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required


from .forms import CookbookCreationForm, RecipeCreationForm, IngredientForm, QuantityForm
from .models import Cookbook


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
        ingredient_form = IngredientForm(request.POST)
        quantity_form = QuantityForm(request.POST)
        # if recipe_form.is_valid() and ingredient_form.is_valid() and quantity_form.is_valid():
        if recipe_form.is_valid():
            recipe = recipe_form.save()
            # Cookbook.objects.create(name=name, user=request.user)
            return redirect('home')
    else:
        form = RecipeCreationForm()

    recipe_form = RecipeCreationForm(request.POST)
    ingredient_form = IngredientForm(request.POST)
    quantity_form = QuantityForm(request.POST)

    context = {
        'recipe_form': recipe_form,
        'ingredient_form': ingredient_form,
        'quantity_form': quantity_form,
    }
    return render(request, 'cookbook/recipe-create.html', context)