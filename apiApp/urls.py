from django.urls import path
from . import views
from django.conf import settings

urlpatterns = [
path('', views.getData),
path('getGenre/<str:anime_name>', views.getGenre),
path('getAllGenre/', views.getAllGenre),
path('pushAnime/', views.pushAnime),
path('pushAnimeGenre/', views.pushAnimeGenre),
path('pushGenre/', views.pushGenre),
]