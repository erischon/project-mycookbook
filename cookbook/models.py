from django.db import models
from django.db.models.fields import IntegerField, URLField
from django.db.models.fields.files import ImageField
from django.db.models.fields.related import ManyToManyField

from accounts.models import CustomUser as User


class Cookbook(models.Model):
    name = models.CharField(max_length=200)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    class Meta:
        unique_together = ['name', 'user']

    def __str__(self):
        return self.name


class LinkType(models.Model):
    name = models.CharField(max_length=200)


class Link(models.Model):
    name = models.CharField(max_length=200)
    url = models.URLField(max_length=200)
    cookbook = models.ForeignKey(Cookbook, on_delete=models.CASCADE)
    linktype = models.ForeignKey(LinkType, on_delete=models.CASCADE)


class Tab(models.Model):
    name = models.CharField(max_length=200)
    cookbook = models.ForeignKey(Cookbook, on_delete=models.CASCADE)


class TagType(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class RecipeType(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Recipe(models.Model):
    title = models.CharField(max_length=200, unique=True)
    description = models.TextField(null=True)
    recipe_type = models.ForeignKey(RecipeType, on_delete=models.CASCADE, blank=True, null=True)
    guest = models.IntegerField(null=True)
    prep_time = models.DurationField(blank=True)
    cook_time = models.DurationField(blank=True)
    source = models.CharField(max_length=200, blank=True)
    cookbook = models.ManyToManyField(Cookbook)

    def __str__(self):
        return self.title


class RecipeInfos(models.Model):
    slug = models.SlugField(max_length=200, null=True)
    private = models.BooleanField(default=True)
    creator = models.ForeignKey(User, on_delete=models.CASCADE, related_name="creator")
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name="owner")
    creation_date = models.DateField(auto_now_add=True)
    modification_date = models.DateField(auto_now=True)
    recipe = models.OneToOneField(Recipe, on_delete=models.CASCADE, null=True)


class Ingredient(models.Model):
    name = models.CharField(max_length=200)
    measure = models.CharField(max_length=50, null=False)
    quantity = models.IntegerField(null=True)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, null=False)

    def __str__(self):
        return str(self.recipe)

    class Meta:
        unique_together = ['name', 'measure', 'quantity', 'recipe']


class Instruction(models.Model):
    step = models.IntegerField(null=False)
    instruction = models.TextField(null=False)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, null=False)


class Tag(models.Model):
    name = models.CharField(max_length=200)
    tagtype = models.ForeignKey(TagType, on_delete=models.CASCADE, null=True)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, null=False)

    def __str__(self):
        return self.name


class Tips(models.Model):
    tips = models.TextField(null=True)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, null=False)


class Photo(models.Model):
    name = models.CharField(max_length=200)
    photo = models.ImageField(null=True, blank=True, upload_to='recipe/')


class Video(models.Model):
    name = models.CharField(max_length=200)
    url = models.URLField(null=True)


class Media(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    photo = models.ForeignKey(Photo, on_delete=models.CASCADE, blank=True)
    video = models.ForeignKey(Video, on_delete=models.CASCADE, blank=True)


class Note(models.Model):
    note = models.TextField(null=True)
    cookbook = models.ForeignKey(Cookbook, on_delete=models.CASCADE)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)


class Favorite(models.Model):
    name = models.CharField(max_length=200)
    cookbook = models.ForeignKey(Cookbook, on_delete=models.CASCADE)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
