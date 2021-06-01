from cookbook.models import Cookbook
from django.http import request
from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth import get_user_model


class CoreTestsViews(TestCase):

    def setUp(self):
        self.client = Client()
        self.user = get_user_model().objects.create_user(
            username='usertest',
            email='usertest@erischon.dev',
            password='testpass123'
        )
        self.client.force_login(self.user)

        self.cb_create_url = reverse('cookbook_create')
        self.r_create_url = reverse('recipe_create')

    def test_cookbook_creation_page_view(self):
        """ """
        response = self.client.get(self.cb_create_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'cookbook/cookbook-create.html')

    def test_cookbook_creation(self):
        """ """
        cb_name = 'a cookbook name'
        query = {'name': cb_name, 'user': self.client}

        response = self.client.post(self.cb_create_url, query)
        cookbook_name = Cookbook.objects.get(name=cb_name)

        self.assertEquals(response.status_code, 302)
        self.assertEquals(cookbook_name.name, cb_name)
        self.assertEquals(cookbook_name.user, self.user)

    def test_recipe_creation_page_view(self):
        """ """
        response = self.client.get(self.r_create_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'cookbook/recipe-create.html')
