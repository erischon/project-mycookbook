from django.shortcuts import render

def recipe_creation(request):
    return render(request, 'cookbook/create.html')
