# Generated by Django 4.2.4 on 2023-09-05 00:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='articl',
            name='anons',
        ),
    ]