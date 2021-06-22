from django.test import TestCase, Client
from django.urls import reverse


class PrivateTestsView(TestCase):

    def setUp(self):

        self.test_notes_list_url = reverse('notes-list', args=[self.recipe.id])

    def test_notes_list_view(self):
        response = self.client.post(self.notes_list_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'private/personal-notes.html')
