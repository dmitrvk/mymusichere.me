# Generated by Django 3.0.4 on 2020-05-01 11:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('scores', '0009_auto_20200408_1809'),
    ]

    operations = [
        migrations.RenameField(
            model_name='score',
            old_name='instrument',
            new_name='instruments',
        ),
    ]
