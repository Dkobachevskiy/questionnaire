# Generated by Django 2.2.19 on 2021-12-13 14:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('question', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='group',
            name='slug',
        ),
    ]