from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required

from cookbook.models import Cookbook, Recipe


def homePage(request):
    """ Home Page. """
    return render(request, 'core/home.html')


@login_required
def user_admin(request):
    """ User Page Administration and Cookbook Creation for the first login. """
    try:
        cookbook = Cookbook.objects.get(user=request.user)
    except Cookbook.DoesNotExist:
        cookbook = Cookbook.objects.create(name=request.user.username, user=request.user)
    return render(request, 'core/user_admin.html', {'cookbook': cookbook})


@login_required
def my_cookbook(request):
    """ Cookbook Page. """
    cookbook_object = Cookbook.objects.get(user=request.user)
    recipes = Recipe.objects.filter(cookbook=cookbook_object)

    return render(request, 'core/mycookbook.html', {'cookbook': cookbook_object, 'recipes': recipes})
