from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth import get_user_model

from social.models import OneTimeLinkModel


class SocialTestsViews(TestCase):

    def setUp(self):
        self.client = Client()

        self.user = get_user_model().objects.create_user(username='usertest', password='testpass123')
        Cookbook.objects.create(name='a cookbook name', user=self.user)

        self.homepage_url = reverse('home')
        self.user_admin_url = reverse('user_admin')
        self.mycookbook_url = reverse('my_cookbook')

    def test_increment_by_one(self):
        """ """
        response = self.client.get(self.homepage_url)

        self.assertEquals(response.status_code, 200)
