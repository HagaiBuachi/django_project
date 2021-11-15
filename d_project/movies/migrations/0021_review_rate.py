# Generated by Django 3.2.7 on 2021-10-16 16:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0020_remove_review_rate'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='rate',
            field=models.PositiveSmallIntegerField(choices=[(1, '1 - Trash'), (2, '2 - Bad'), (3, '3 - OK'), (4, '4 - Very Good'), (5, '5 - Master Piece')], null=True),
        ),
    ]
