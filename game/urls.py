from django.urls import path
from . import views

urlpatterns = [
    path('', views.game_home, name='game_home'),
    path('create_game', views.create_game, name='create_game'),
    path('<int:pk>', views.GameDetailView.as_view(), name='game-detail'),
    path('<int:pk>/update', views.GameUpdateView.as_view(), name='game-update'),
    path('<int:pk>/delete', views.GameDeleteView.as_view(), name='game-delete'),
]