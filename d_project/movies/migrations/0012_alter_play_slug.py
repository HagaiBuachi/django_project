# Generated by Django 3.2.7 on 2021-10-11 17:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0011_play_author'),
    ]

    operations = [
        migrations.AlterField(
            model_name='play',
            name='slug',
            field=models.SlugField(default=3),
            preserve_default=False,
        ),
    ]
