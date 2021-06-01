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


class Ingredient(models.Model):
    name = models.CharField(max_length=200)


class TagType(models.Model):
    name = models.CharField(max_length=200)


class Tag(models.Model):
    name = models.CharField(max_length=200)
    tagtype = models.ForeignKey(TagType, on_delete=models.CASCADE)


class Recipe(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(null=True)
    guest = models.IntegerField(null=True)
    prep_time = models.DurationField(blank=True)
    cook_time = models.DurationField(blank=True)
    source = models.CharField(max_length=200, blank=True)
    cookbook = models.ManyToManyField(Cookbook)
    ingredient = models.ManyToManyField(Ingredient)
    tags = models.ManyToManyField(Tag, blank=True)


class RecipeInfos(models.Model):
    slug = models.SlugField(max_length=200, null=True)
    private = models.BooleanField(default=True)
    creator = models.ForeignKey(User, on_delete=models.CASCADE, related_name="creator")
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name="owner")
    creation_date = models.DateField(auto_now_add=True)
    modification_date = models.DateField(auto_now=True)


class Quantity(models.Model):
    measure = models.CharField(max_length=200)
    quantity = models.IntegerField(null=True)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)


class Instruction(models.Model):
    step = models.IntegerField(null=True)
    instruction = models.TextField(null=True)
    cookbook = models.ForeignKey(Cookbook, on_delete=models.CASCADE)


class Tips(models.Model):
    tips = models.TextField(null=True)
    cookbook = models.ForeignKey(Cookbook, on_delete=models.CASCADE)


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
