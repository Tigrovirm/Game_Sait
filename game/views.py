from django.shortcuts import render, redirect
from .models import Articl
from .forms import ArticlForm
from django.views.generic import DetailView, UpdateView, DeleteView


def game_home(request):
    game = Articl.objects.order_by('-date')
    return render(request, 'game/game_home.html', {'game': game})

class GameDetailView(DetailView):
    model = Articl
    template_name = 'game/details_view.html'
    context_object_name = 'article'


class GameUpdateView(UpdateView):
    model = Articl
    template_name = 'game/create_game.html'

    form_class = ArticlForm

class GameDeleteView(DeleteView):
    model = Articl
    success_url = '/game/'
    template_name = 'game/delete_game.html'


def create_game(request):
    error = ''
    if request.method == 'POST':
        form = ArticlForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = 'Форма была неверной'

    form = ArticlForm()

    data = {
        'form': form
    }

    return render(request, 'game/create_game.html', data)