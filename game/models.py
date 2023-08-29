from django.db import models


class Articl(models.Model):
    title = models.CharField('Название', max_length=50, default= None)
    anons = models.CharField('Анонс', max_length=250, default=None)
    full_text =models.TextField('Об игре', default=None)
    date = models.DateTimeField('Дата Публикации', default=None)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return f'/game/{self.id}'
    
    class Meta:
        verbose_name = 'Игра'
        verbose_name_plural = 'Игры'