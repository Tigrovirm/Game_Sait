from django.urls import path, include
from . import views

app_name = 'game'

urlpatterns = [
    path('', views.game_home, name='game_home'),
    path('', include('django.contrib.auth.urls')),
    path('create_game', views.create_game, name='create_game'),
    path('<int:pk>', views.GameDetailView.as_view(), name='game-detail'),
    path('<int:pk>/update', views.GameUpdateView.as_view(), name='game-update'),
    path('<int:pk>/delete', views.GameDeleteView.as_view(), name='game-delete'),
    path('registеr/', views.register, name='register'),
    path('staff/', views.staff, name='staff'),
]