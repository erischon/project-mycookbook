from django.shortcuts import redirect, render
# from django.http import HttpResponseRedirect

from .forms import CookbookCreationForm
from .models import Cookbook


def cookbook_creation(request):
    return render(request, 'cookbook/cookbook-create.html')


def recipe_creation(request):
    return render(request, 'cookbook/recipe-create.html')


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
