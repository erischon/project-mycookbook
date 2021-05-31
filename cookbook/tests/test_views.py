from django.test import TestCase, Client
from django.urls import reverse


class CoreTestsViews(TestCase):

    def setUp(self):
        self.client = Client()

        self.cb_create_url = reverse('cookbook_create')
        self.r_create_url = reverse('recipe_create')

    def test_cookbook_creation_view(self):
        """ """
        response = self.client.get(self.cb_create_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'cookbook/cookbook-create.html')

    def test_recipe_creation_view(self):
        """ """
        response = self.client.get(self.r_create_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'cookbook/recipe-create.html')
