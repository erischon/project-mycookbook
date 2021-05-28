from django.contrib.auth import get_user_model
from django.test import TestCase


class CustomUserTests(TestCase):

    def setUp(self):
        self.client = get_user_model()

    def test_create_user(self):
        """ """
        
        response = get_user_model().objects.create_user(
            username='test',
            email='test@erischon.dev',
            password='testpass123'
        )

        self.assertEqual(response.username, 'test')
        self.assertEqual(response.email, 'test@erischon.dev')
        self.assertTrue(response.check_password('testpass123'))
        self.assertTrue(response.is_active)
        self.assertFalse(response.is_staff)
        self.assertFalse(response.is_superuser)
