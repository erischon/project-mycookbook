from django.http import request
from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth import get_user_model

from cookbook.forms import RecipeCreationForm
from cookbook.models import Cookbook, Recipe, RecipeInfos


class CookbookTestViews(TestCase):

    def setUp(self):
        self.client = Client()
        self.client_b = Client()
        # Users
        self.user = get_user_model().objects.create_user(
            username='usertest',
            email='usertest@erischon.dev',
            password='testpass123'
        )
        self.user_b = get_user_model().objects.create_user(
            username='user test b',
            email='usertestb@erischon.dev',
            password='testpass123'
        )
        self.client.force_login(self.user)
        self.client_b.force_login(self.user_b)

        # Cookbook
        self.cookbook = Cookbook.objects.create(
            name='Cookbook test',
            user=self.user_b,
        )
        # Recipe
        self.recipe = Recipe.objects.create (
            title='Recette test',
            description='Une description Test',
            guest=3,
            prep_time='0:5:0',
            cook_time='0:5:0',
            source='Aucune',
        )
        self.recipeinfos = RecipeInfos.objects.create (
            creator=self.user,
            owner=self.user,
            slug='recette-test',
            recipe=self.recipe,
        )

        self.cb_create_url = reverse('cookbook_create')
        self.r_create_url = reverse('recipe_create')
        self.recipe_page_url = reverse('recipe-detail', args=[self.recipe.id])

    def test_cookbook_creation_page_view(self):
        """ """
        response = self.client.get(self.cb_create_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'cookbook/cookbook-create.html')

    def test_cookbook_creation(self):
        """ """
        cb_name = 'a cookbook name'
        query = {'name': cb_name, 'user': self.client_b}

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

    def test_cookbook_recipe_detail_page_view(self):
        """ """
        response = self.client.get(self.recipe_page_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'cookbook/recipe-detail.html')


class CreateRecipeTestPostView(TestCase):

    # l'utilisateur doit être log
    # valider la method POST
    # valider qu'il est bien redirigé vers home

    def setUp(self):
        self.client = Client()
        # Users
        self.user = get_user_model().objects.create_user(
            username='usertest',
            email='usertest@erischon.dev',
            password='testpass123'
        )
        self.client.force_login(self.user)
        self.cookbook = Cookbook.objects.create(
            name='Cookbook test',
            user=self.user,
        )

        self.recipe_create_url = reverse('recipe_create')

    def test_recipe_creation_POST(self):
        """ Test the recipe creation in database. """
        response = self.client.post(self.recipe_create_url, {
            'recipe_form': 'True', 'title': 'Recette test', 'description': 'none', 'guest': '1', 'prep_time': '5:00', 'cook_time': '5:00', 'source': 'none',
            'ingredient_formset': 'True', 'name': 'ingredient test', 'measure': 'kg', 'quantity': '1',
            'instruction_formset': 'True', 'step': '1', 'instruction': 'none',
             'tag_formset': 'True', 'name': 'tag test', 'tagtype': 'type',
        })

        self.assertEquals(response.status_code, 302)
        # self.assertTemplateUsed(response, 'cookbook/recipe-create.html')
