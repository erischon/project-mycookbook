# Generated by Django 3.2.3 on 2021-06-01 06:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cookbook', '0002_alter_recipeinfos_owner'),
    ]

    operations = [
        migrations.AddField(
            model_name='instruction',
            name='instruction',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='instruction',
            name='step',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='note',
            name='note',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='quantity',
            name='quantity',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='recipe',
            name='description',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='recipe',
            name='guest',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='recipeinfos',
            name='modification_date',
            field=models.DateField(auto_now=True),
        ),
        migrations.AddField(
            model_name='recipeinfos',
            name='slug',
            field=models.SlugField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='tips',
            name='tips',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='video',
            name='url',
            field=models.URLField(null=True),
        ),
    ]
