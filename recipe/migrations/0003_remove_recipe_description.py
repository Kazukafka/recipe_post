# Generated by Django 3.2.7 on 2021-09-15 12:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recipe', '0002_auto_20210915_2121'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='recipe',
            name='description',
        ),
    ]