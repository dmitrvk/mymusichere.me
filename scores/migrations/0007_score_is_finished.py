# Generated by Django 3.0.4 on 2020-03-31 11:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scores', '0006_auto_20200329_1058'),
    ]

    operations = [
        migrations.AddField(
            model_name='score',
            name='is_finished',
            field=models.BooleanField(default=True),
        ),
    ]
