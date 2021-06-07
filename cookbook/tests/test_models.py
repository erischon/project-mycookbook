from django.test import TestCase, Client
from django.contrib.auth import get_user_model

from cookbook.models import Cookbook, Recipe, TagType, Tag, Ingredient


class CookbookModelsTest(TestCase):

    def setUp(self):
        self.client = Client()
        # User
        self.user = get_user_model().objects.create_user(
            username='usertest',
            email='usertest@erischon.dev',
            password='testpass123'
        )
        self.cookbook = Cookbook.objects.create(
            name='Cookbook test',
            user=self.user,
        )
        self.recipe = Recipe.objects.create (
            title='Recette test',
            description='Une description Test',
            guest=3,
            prep_time='0:5:0',
            cook_time='0:5:0',
            source='Aucune',
        )
        self.ingredient = Ingredient.objects.create(
            name='Ingrédient 1',
            measure='kg',
            quantity='1',
            recipe=self.recipe
        )
        self.tagtype = TagType.objects.create(
            name='Tag Type de test'
        )
        self.tag = Tag.objects.create(
            name='Tag Type de test',
            tagtype=self.tagtype,
            recipe=self.recipe,
        )

    def test_cookbook_name(self):
        """ """
        cookbook = Cookbook.objects.get(user=self.user)
        cookbook_name = cookbook.name

        self.assertEquals(cookbook_name, str(cookbook))

    def test_recipe_name(self):
        """ """
        recipe = Recipe.objects.get(title='Recette test')
        recipe_name = recipe.title

        self.assertEquals(recipe_name, str(recipe))

    def test_ingredient_name(self):
        """ """
        ingredient = Ingredient.objects.get(name='Ingrédient 1')
        ingredient_name = str(ingredient.recipe)

        self.assertEquals(ingredient_name, str(ingredient))

    def test_tagtype_name(self):
        """ """
        tagtype = TagType.objects.get(name='Tag Type de test')
        tagtype_name = tagtype.name

        self.assertEquals(tagtype_name, str(tagtype))

    def test_tag_name(self):
        """ """
        tag = Tag.objects.get(name='Tag Type de test')
        tag_name = tag.name

        self.assertEquals(tag_name, str(tag))