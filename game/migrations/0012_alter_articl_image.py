# Generated by Django 4.2.4 on 2023-09-03 12:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0011_alter_articl_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articl',
            name='image',
            field=models.FileField(blank=True, null=True, upload_to='images', verbose_name='Изображение'),
        ),
    ]