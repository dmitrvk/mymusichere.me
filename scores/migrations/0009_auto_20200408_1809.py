# Generated by Django 3.0.4 on 2020-04-08 18:09

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scores', '0008_remove_score_is_finished'),
    ]

    operations = [
        migrations.AddField(
            model_name='score',
            name='arranger',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AddField(
            model_name='score',
            name='composer',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AddField(
            model_name='score',
            name='instrument',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AddField(
            model_name='score',
            name='last_modified',
            field=models.DateTimeField(default=datetime.datetime(2020, 1, 1, 0, 0)),
        ),
        migrations.AddField(
            model_name='score',
            name='views',
            field=models.IntegerField(default=0),
        ),
    ]