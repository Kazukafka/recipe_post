# Generated by Django 3.2.7 on 2021-09-15 12:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipe', '0003_remove_recipe_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='description',
            field=models.TextField(blank=True, default=''),
        ),
    ]