from django.urls import path
from . import views

urlpatterns = [
    path('', views.homePage, name='home'),
    path('user-admin/', views.user_admin, name='user_admin'),
    path('mycookbook/', views.my_cookbook, name='my_cookbook'),
]
