# Generated by Django 3.2.7 on 2021-10-08 07:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0008_alter_movies_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movies',
            name='category',
            field=models.CharField(choices=[('A', 'Action'), ('D', 'Drama')], max_length=10),
        ),
    ]
