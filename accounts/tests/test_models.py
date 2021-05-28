from django.contrib.auth import get_user_model
from django.test import TestCase


class CustomUserTests(TestCase):

    def setUp(self):
        User = get_user_model()
        self.user = User.objects.create_user(
            username='test',
            email='test@erischon.dev',
            password='testpass123'
        )

    def test_create_user(self):
        """ """
        self.assertEqual(self.user.username, 'test')
        self.assertEqual(self.user.email, 'test@erischon.dev')
        self.assertTrue(self.user.is_active)
        self.assertFalse(self.user.is_staff)
        self.assertFalse(self.user.is_superuser)
