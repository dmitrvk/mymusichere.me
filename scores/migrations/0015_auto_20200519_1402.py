# Generated by Django 3.0.4 on 2020-05-19 14:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('scores', '0014_auto_20200518_1132'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='instrument',
            options={'ordering': ['name']},
        ),
    ]
