# Generated by Django 3.2.7 on 2021-11-06 17:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0026_remove_review_rate'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='slug',
            field=models.SlugField(null=True, unique=True),
        ),
    ]