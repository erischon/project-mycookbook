from django.test import TestCase, Client
from django.urls import reverse


class CoreTestsViews(TestCase):

    def setUp(self):
        self.client = Client()

        self.homepage_url = reverse('home')

    def test_homepage_view(self):
        """ """
        response = self.client.get(self.homepage_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'core/home.html')
