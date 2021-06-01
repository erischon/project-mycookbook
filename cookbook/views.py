from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required

# from django.http import HttpResponseRedirect

from .forms import CookbookCreationForm
from .models import Cookbook


@login_required
def recipe_creation(request):
    return render(request, 'cookbook/recipe-create.html')


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
