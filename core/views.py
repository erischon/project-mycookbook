from django.shortcuts import render

from cookbook.models import Cookbook


def homePage(request):
    return render(request, 'core/home.html')

def user_admin(request):
    cookbook = Cookbook.objects.get(user=request.user)
    return render(request, 'core/user_admin.html', {'cookbook': cookbook})

def my_cookbook(request):
    cookbook = Cookbook.objects.get(user=request.user)
    return render(request, 'core/mycookbook.html', {'cookbook': cookbook})