from cookbook.forms import IngredientForm
from django.test import TestCase


class CookbookTestForms(TestCase):

    def test_ingredient_form(self):
        """ """
        query = {
            'name': 'ingredient test', 'measure': 'kg', 'quantity': '1',
        }
        form = IngredientForm(query)

        self.assertTrue(form.is_valid())
