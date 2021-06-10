from django.db.models import query
from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.forms import ModelForm, modelformset_factory
from django.utils.text import slugify
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView, CreateView
from django.contrib import messages
from django.http import HttpResponseRedirect


from .forms import CookbookCreationForm, RecipeCreationForm, IngredientForm, InstructionForm, TagForm
from .models import Cookbook, Recipe, Ingredient, RecipeInfos, Instruction, Tag, TagType


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
    InstructionFormSet = modelformset_factory(Instruction, form=InstructionForm)
    TagFormSet = modelformset_factory(Tag, form=TagForm)
    data_ingredient = {
        'ingredient-TOTAL_FORMS': '1',
        'ingredient-INITIAL_FORMS': '0',
    }
    data_instruction = {
        'instruction-TOTAL_FORMS': '1',
        'instruction-INITIAL_FORMS': '0',
    }
    data_tag = {
        'tag-TOTAL_FORMS': '1',
        'tag-INITIAL_FORMS': '0',
    }

    if request.method == 'POST':
        recipe_form = RecipeCreationForm(request.POST)
        ingredient_formset = IngredientFormSet(request.POST, prefix='ingredient')
        instruction_formset = InstructionFormSet(request.POST, prefix='instruction')
        tag_formset = TagFormSet(request.POST, prefix='tag')

        if recipe_form.is_valid() and ingredient_formset.is_valid() and instruction_formset.is_valid():
            # Recipe
            recipe = recipe_form.save()
            recipe.cookbook.set([Cookbook.objects.get(user=request.user)])
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
            # Instructions
            instructions = instruction_formset.save(commit=False)
            for instruction in instructions:
                instruction.recipe = recipe
                instruction.save()
            # Tags
            tags = tag_formset.save(commit=False)
            for tag in tags:
                tag.recipe = recipe
                tag.save()

            return redirect('my_cookbook')

    else:
        recipe_form = RecipeCreationForm()
        ingredient_formset = IngredientFormSet(data_ingredient, prefix='ingredient')
        instruction_formset = InstructionFormSet(data_instruction, prefix='instruction')
        tag_formset = TagFormSet(data_tag, prefix='tag')

    context = {
        'recipe_form': recipe_form,
        'ingredient_formset': ingredient_formset,
        'instruction_formset': instruction_formset,
        'tag_formset': tag_formset,
    }
    return render(request, 'cookbook/recipe-create.html', context)


@login_required
def update_recipe(request, pk):
    # Formsets
    IngredientFormSet = modelformset_factory(Ingredient, form=IngredientForm, extra=0)
    InstructionFormSet = modelformset_factory(Instruction, form=InstructionForm, extra=0)
    TagFormSet = modelformset_factory(Tag, form=TagForm, extra=0)
    # Query
    recipe = Recipe.objects.get(id=pk)
    ingredient_queryset = Ingredient.objects.filter(recipe=recipe)
    instruction_queryset = Instruction.objects.filter(recipe=recipe)
    tag_queryset = Tag.objects.filter(recipe=recipe)
    # Form
    recipe_form = RecipeCreationForm(request.POST, instance=recipe)
    ingredient_formset = IngredientFormSet(request.POST, prefix='ingredient', queryset=ingredient_queryset)
    instruction_formset = InstructionFormSet(request.POST, prefix='instruction', queryset= instruction_queryset)
    tag_formset = TagFormSet(request.POST, prefix='tag', queryset=tag_queryset)

    if recipe_form.is_valid() and ingredient_formset.is_valid() and instruction_formset.is_valid():
        # Recipe
        recipe = recipe_form.save()
        recipe.cookbook.set([Cookbook.objects.get(user=request.user)])
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
        # Instructions
        instructions = instruction_formset.save(commit=False)
        for instruction in instructions:
            instruction.recipe = recipe
            instruction.save()
        # Tags
        tags = tag_formset.save(commit=False)
        for tag in tags:
            tag.recipe = recipe
            tag.save()

        return redirect('my_cookbook')

    context = {
        'recipe_form': recipe_form,
        'ingredient_formset': ingredient_formset,
        'instruction_formset': instruction_formset,
        'tag_formset': tag_formset,
    }
    return render(request, 'cookbook/recipe-create.html', context)


class RecipeDetailView(DetailView):

    model = Recipe
    template_name = 'cookbook/recipe-detail.html'
    context_object_name = 'recipe'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['infos'] = RecipeInfos.objects.get(recipe=context['object'])
        context['ingredients'] = Ingredient.objects.filter(recipe=context['object'])
        context['instructions'] = Instruction.objects.filter(recipe=context['object'])
        context['tags'] = Tag.objects.filter(recipe=context['object'])

        return context
