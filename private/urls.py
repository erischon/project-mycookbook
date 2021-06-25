from django.urls import path
from django.contrib.auth.decorators import login_required

from .views import CreateNoteView, DeleteNoteView, NoteListView


urlpatterns = [
    path('<int:pk>/note/', login_required(NoteListView.as_view()), name='note-list'),
    path('<int:pk>/note/create', login_required(CreateNoteView.as_view()), name='create-note'),
    path('note/delete/<int:pk>', login_required(DeleteNoteView.as_view()), name='delete-note'),
]
