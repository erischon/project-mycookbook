from django.db import models
from django.utils.translation import gettext_lazy as _

from cookbook.models import Cookbook, Recipe


class PersonalNote(models.Model):
    """ Personal Note Model. """
    NUL = 'Nul'
    BOF = 'Bof'
    MOYEN = 'Moyen'
    TOP = 'Top'
    SUPER = 'Super'
    SATISFACTION_CHOICES = [
        (NUL, 'J\'aime pas du tout'),
        (BOF, 'C\'est bof'),
        (MOYEN, 'Ca va'),
        (TOP, 'C\'est bon'),
        (SUPER, 'Vraiment succulent'),
    ]

    note = models.TextField(null=True)
    date = models.DateField(auto_now_add=True)
    satisfaction = models.CharField(max_length=5, choices=SATISFACTION_CHOICES, default=MOYEN)
    cookbook = models.ForeignKey(Cookbook, on_delete=models.CASCADE)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
