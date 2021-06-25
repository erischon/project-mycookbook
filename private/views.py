from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, DeleteView
from django.urls.base import reverse_lazy


from cookbook.models import Recipe, RecipeInfos, Cookbook
from private.models import PersonalNote
from private.forms import NoteCreationForm


class CreateNoteView(CreateView):
    model = PersonalNote
    form_class = NoteCreationForm
    template_name = 'private/note-form.html'
    success_url = 'home'

    def form_valid(self, form):
        form.save(commit=False)
        recipe = Recipe.objects.get(pk=self.kwargs.get('pk'))
        cookbook = recipe.cookbook.get()
        form.instance.recipe = recipe
        form.instance.cookbook = cookbook
        return super(CreateNoteView, self).form_valid(form)

    def get_success_url(self):
        return reverse_lazy('note-list', args=(self.object.recipe.id,))

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        recipe = Recipe.objects.get(pk=self.kwargs.get('pk'))
        context['recipe'] = recipe
        return context


class NoteListView(ListView):
    model = PersonalNote
    template_name = 'private/note-list.html'

    def get_queryset(self):
        return PersonalNote.objects.filter(recipe=self.kwargs.get('pk')).order_by('-date')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        recipe = Recipe.objects.get(pk=self.kwargs.get('pk'))
        context['recipe'] = recipe
        return context


class DeleteNoteView(DeleteView):
    model = PersonalNote

    def get_success_url(self):
        return reverse_lazy('note-list', args=(self.object.recipe.id,))

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        note = PersonalNote.objects.get(pk=self.kwargs.get('pk'))
        recipe = note.recipe
        context['recipe'] = recipe
        return context
