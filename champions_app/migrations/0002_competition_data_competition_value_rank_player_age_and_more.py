# Generated by Django 4.0.3 on 2022-03-31 18:07

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('champions_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='competition',
            name='data',
            field=models.DateTimeField(blank=True, default=datetime.datetime.now),
        ),
        migrations.AddField(
            model_name='competition',
            name='value_rank',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='player',
            name='age',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='player',
            name='height',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='player',
            name='weight',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='team',
            name='number_of_players',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='team',
            name='rank',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
