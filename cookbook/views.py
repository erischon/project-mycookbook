from django.shortcuts import render
from django.http import HttpResponseRedirect

from .forms import CookbookCreationForm


def cookbook_creation(request):
    return render(request, 'cookbook/cookbook-create.html')

def recipe_creation(request):
    return render(request, 'cookbook/recipe-create.html')

def create_cookbook(request):
    if request.method == 'POST':
        form = CookbookCreationForm(request.POST)
        if form.is_valid():
            return HttpResponseRedirect('home')
    else:
        form = CookbookCreationForm()

    return render(request, 'cookbook/cookbook-create.html', {'form': form})
