from django.forms import ModelForm

from .models import PersonalNote


class NoteCreationForm(ModelForm):
    """ Note creation Form. """
    class Meta:
        model = PersonalNote
        fields = ['note', 'satisfaction']
        labels = {
            'note': 'Note personnelle ',
            'satisfaction': 'Appréciation ',
        }
