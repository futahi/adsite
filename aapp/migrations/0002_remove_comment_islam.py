# Generated by Django 3.2 on 2021-04-19 10:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('aapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='islam',
        ),
    ]