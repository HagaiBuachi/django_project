# Generated by Django 3.2.7 on 2021-10-10 19:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0009_alter_movies_category'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Movies',
            new_name='Play',
        ),
    ]
