from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView
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
        return reverse_lazy('recipe-detail', args=(self.object.recipe.id,))

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        recipe = Recipe.objects.get(pk=self.kwargs.get('pk'))
        context['recipe'] = recipe
        return context


class NoteListView(ListView):
    pass


class UpdateNoteView(UpdateView):
    pass
