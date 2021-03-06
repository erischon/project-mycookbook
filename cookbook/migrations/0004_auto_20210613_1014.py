# Generated by Django 3.2.3 on 2021-06-13 08:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cookbook', '0003_alter_tag_tagtype'),
    ]

    operations = [
        migrations.AlterField(
            model_name='instruction',
            name='instruction',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='instruction',
            name='step',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='tag',
            name='tagtype',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='cookbook.tagtype'),
        ),
    ]
