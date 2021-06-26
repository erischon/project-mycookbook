from django.test import TestCase, Client
from django.contrib.auth import get_user_model
from django.urls import reverse

from cookbook.models import Cookbook, Recipe, RecipeInfos


class PrivateTestsView(TestCase):

    def setUp(self):
        self.client = Client()
        # Users
        self.user = get_user_model().objects.create_user(
            username='usertest',
            email='usertest@erischon.dev',
            password='testpass123'
        )
        self.client.force_login(self.user)
        # Cookbook
        self.cookbook = Cookbook.objects.create(
            name='Cookbook test',
            user=self.user,
        )
        # Recipe
        self.recipe = Recipe.objects.create(
            title='Recette test',
            description='Une description Test',
            guest=3,
            prep_time='0:5:0',
            cook_time='0:5:0',
            source='Aucune',
        )
        self.recipe.cookbook.add(self.cookbook)
        self.recipeinfos = RecipeInfos.objects.create(
            creator=self.user,
            owner=self.user,
            slug='recette-test',
            recipe=self.recipe,
        )
        # Urls
        self.note_create_url = reverse('create-note', args=[self.recipe.id])
        self.note_list_url = reverse('note-list', args=[self.recipe.id])

    def test_note_create_view(self):
        kwargs = {
            'note': 'Quelques mots',
            'satisfaction': 'Moyen',
        }
        success_url = "/private/{}/note/".format(self.recipe.id)

        response = self.client.post(self.note_create_url)
        response_2 = self.client.post(self.note_create_url, kwargs)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'private/note-form.html')
        self.assertRedirects(response_2, success_url)

    def test_note_list_view(self):
        response = self.client.get(self.note_list_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'private/note-list.html')

    def test_note_delete_view(self):
        pass
