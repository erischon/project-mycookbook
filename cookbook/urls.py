from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.recipe_creation, name='recipe_create'),
]
