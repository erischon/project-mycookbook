from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth import get_user_model

from cookbook.models import Cookbook


class CoreTestsViews(TestCase):

    def setUp(self):
        self.client = Client()

        self.user = get_user_model().objects.create_user(username='usertest', password='testpass123')
        Cookbook.objects.create(name='a cookbook name', user=self.user)

        self.homepage_url = reverse('home')
        self.user_admin_url = reverse('user_admin')
        self.mycookbook_url = reverse('my_cookbook')

    def test_homepage_view(self):
        """ """
        response = self.client.get(self.homepage_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'core/home.html')

    def test_user_admin_view(self):
        """ """
        self.client.force_login(self.user)

        response = self.client.get(self.user_admin_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'core/user_admin.html')

    def test_mycookbook_view(self):
        """ """
        self.client.force_login(self.user)

        response = self.client.get(self.mycookbook_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'core/mycookbook.html')