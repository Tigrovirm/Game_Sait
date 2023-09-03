from .models import Articl
from django.forms import ModelForm, TextInput, DateTimeInput, Textarea, FileInput

class ArticlForm(ModelForm):
    class Meta:
        model = Articl
        fields = ['title', 'anons', 'full_text', 'date', 'image']

        widgets = {
            "title": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Название Игры'
            }),
            "anons": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Анонс Игры'
            }),
            "date": DateTimeInput(attrs={
                'class': 'form-control',
                'placeholder': 'Дата Выхода'
            }),
            "image": FileInput(attrs={
                'class': 'form-control',
                'placeholder': 'Путь изображения'
            }),
            "full_text": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Об Игре'
            })
        }