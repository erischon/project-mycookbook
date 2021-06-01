from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from cookbook.models import Cookbook


def homePage(request):
    return render(request, 'core/home.html')


@login_required
def user_admin(request):
    cookbook = Cookbook.objects.get(user=request.user)
    return render(request, 'core/user_admin.html', {'cookbook': cookbook})


@login_required
def my_cookbook(request):
    cookbook = Cookbook.objects.get(user=request.user)
    return render(request, 'core/mycookbook.html', {'cookbook': cookbook})
