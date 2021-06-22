from django.urls import path
from django.contrib.auth.decorators import login_required

from .views import NotesList


urlpatterns = [
    path('<int:pk>/notes', login_required(NotesList.as_view()), name='notes-list'),
]
