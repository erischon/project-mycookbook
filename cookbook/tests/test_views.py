from django.http import request
from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth import get_user_model

from cookbook.forms import RecipeCreationForm
from cookbook.models import Cookbook, Recipe, RecipeInfos, TagType, Ingredient, Instruction, Tag


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
        self.recipe = Recipe.objects.create(
            title='Recette test',
            description='Une description Test',
            guest=3,
            prep_time='0:5:0',
            cook_time='0:5:0',
            source='Aucune',
        )
        self.recipeinfos = RecipeInfos.objects.create(
            creator=self.user,
            owner=self.user,
            slug='recette-test',
            recipe=self.recipe,
        )
        # Ingredient
        self.ingredient = Ingredient.objects.create(
            name="ingredient name",
            measure="une mesure",
            quantity='1',
            recipe=self.recipe,
        )
        # Instruction
        self.instruction = Instruction.objects.create(
            step="1",
            instruction="une instruction",
            recipe=self.recipe,
        )
        # TagType
        self.tagtype = TagType.objects.create(
            id=1,
            name='tagtype test',
        )
        # Tag
        self.tag = Tag.objects.create(
            name="tag test",
            tagtype=self.tagtype,
            recipe=self.recipe,
        )
        # Urls
        self.cb_create_url = reverse('cookbook_create')
        self.r_create_url = reverse('recipe_create')
        self.recipe_page_url = reverse('recipe-detail', args=[self.recipe.id])
        self.recipe_detail_edit_mode_url = reverse('recipe-edit-mode', args=[self.recipe.id])
        self.recipe_edit_url = reverse('recipe-edit', args=[self.recipe.id])
        self.ingredient_edit_url = reverse('ingredient-edit', args=[self.ingredient.id])
        self.ingredient_add_url = reverse('ingredient-add', args=[self.recipe.id])
        self.instruction_edit_url = reverse('instruction-edit', args=[self.instruction.id])
        self.instruction_add_url = reverse('instruction-add', args=[self.recipe.id])
        self.tag_edit_url = reverse('tag-edit', args=[self.tag.id])
        self.tag_add_url = reverse('tag-add', args=[self.recipe.id])


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

    """
    Testing the CBV for Recipe Edit and Add part.
    """
    def test_recipe_detail_edit_mode(self):
        """
        cette class doit
        afficher la page
        avec les informations existantes
        """
        response = self.client.get(self.recipe_detail_edit_mode_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'cookbook/recipe-detail-edit-mode.html')

    def test_recipe_edit(self):
        """
        cette class doit
        afficher le formulaire
        avec les informations existantes
        sauvegarder les modifications
        revenir sur la page de la recette en mode édition
        """
        response = self.client.get(self.recipe_edit_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'cookbook/recipe-edit.html')

    def test_ingredient_edit(self):
        response = self.client.get(self.ingredient_edit_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'cookbook/recipe-edit.html')

    def test_ingredient_add(self):
        kwargs = {
            'name': 'Ingredient add',
            'measure': 'measure add',
            'quantity': '1',
        }
        success_url = "/cookbook/{}/detail/edit".format(self.recipe.id)

        response = self.client.get(self.ingredient_add_url)
        response_2 = self.client.post(self.ingredient_add_url, kwargs)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'cookbook/recipe-edit.html')
        self.assertRedirects(response_2, success_url)

    def test_instruction_edit(self):
        response = self.client.get(self.instruction_edit_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'cookbook/recipe-edit.html')

    def test_instruction_add(self):
        kwargs = {
            'step': '1',
            'instruction': 'instruction add',
        }
        success_url = "/cookbook/{}/detail/edit".format(self.recipe.id)

        response = self.client.get(self.instruction_add_url)
        response_2 = self.client.post(self.instruction_add_url, kwargs)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'cookbook/recipe-edit.html')
        self.assertRedirects(response_2, success_url)

    def test_tag_edit(self):
        response = self.client.get(self.tag_edit_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'cookbook/recipe-edit.html')

    def test_tag_add(self):
        kwargs = {
            'name': 'tagg add',
            'tagtype': '1',
        }
        success_url = "/cookbook/{}/detail/edit".format(self.recipe.id)

        response = self.client.get(self.tag_add_url)
        response_2 = self.client.post(self.tag_add_url, kwargs)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'cookbook/recipe-edit.html')
        self.assertRedirects(response_2, success_url)


class CreateRecipeTestPostView(TestCase):

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
        # Tagtype
        self.tagtype = TagType.objects.create(
            id=1,
            name='tagtype',
        )

        self.recipe_create_url = reverse('recipe_create')

    def test_recipe_creation_POST(self):
        """ Test the recipe creation in database. """
        kwargs = {
            'title': 'Recette test', 'description': 'none', 'guest': '1', 'prep_time': '5:00', 'cook_time': '5:00', 'source': 'none',
            'ingredient-TOTAL_FORMS': '1', 'ingredient-INITIAL_FORMS': '0', 'ingredient-0-name': 'ingredient test', 'ingredient-0-measure': 'kg', 'ingredient-0-quantity': '1',
            'instruction-TOTAL_FORMS': '1', 'instruction-INITIAL_FORMS': '0', 'instruction-0-step': '1', 'instruction-0-instruction': 'none',
            'tag-TOTAL_FORMS': '1', 'tag-INITIAL_FORMS': '0', 'tag-0-name': 'tag test', 'tag-0-tagtype': '1',
        }

        response = self.client.post(self.recipe_create_url, kwargs)

        self.assertEquals(response.status_code, 302)
        self.assertRedirects(response, '/mycookbook/')
