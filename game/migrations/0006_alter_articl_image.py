# Generated by Django 4.2.4 on 2023-09-03 11:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0005_alter_articl_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articl',
            name='image',
            field=models.ImageField(default=1, upload_to='img/', verbose_name='Изображение'),
            preserve_default=False,
        ),
    ]