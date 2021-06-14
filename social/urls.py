from django.urls import path
from . import views


urlpatterns = [
    path('share-link/<int:id>', views.generate_link, name='share-link'),
    path('otl/<int:id>/<str:access_code>', views.one_time_link, name='one-time-link'),
]
