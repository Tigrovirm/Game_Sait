# Generated by Django 4.2.4 on 2023-09-03 13:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0012_alter_articl_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articl',
            name='image',
            field=models.FileField(default=None, upload_to='images', verbose_name='Изображение'),
        ),
    ]