from django.urls import path
from . import views


urlpatterns = [
    path('generate_link', views.generate_link, name='generate-link'),
    path('one_time_link/<str:access_code>', views.one_time_link, name='one-time-link'),
]
