from django.test import TestCase, Client
from django.urls import reverse


class CoreTestsViews(TestCase):

    def setUp(self):
        self.client = Client()

        self.create_url = reverse('recipe_create')

    def test_recipe_creation_view(self):
        """ """
        response = self.client.get(self.create_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'cookbook/create.html')
