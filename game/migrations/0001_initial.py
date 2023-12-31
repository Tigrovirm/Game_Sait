# Generated by Django 4.2.4 on 2023-09-05 00:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Articl',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default=None, max_length=50, verbose_name='Название')),
                ('anons', models.CharField(default=None, max_length=250, verbose_name='Анонс')),
                ('full_text', models.TextField(default=None, verbose_name='Об игре')),
                ('image', models.ImageField(blank=True, null=True, upload_to='images/', verbose_name='Изображение')),
                ('date', models.DateTimeField(default=None, verbose_name='Дата Публикации')),
            ],
            options={
                'verbose_name': 'Игра',
                'verbose_name_plural': 'Игры',
            },
        ),
    ]
