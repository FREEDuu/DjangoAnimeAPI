from rest_framework import serializers
from apiApp.models import Anime, Genre, GenreAnime

class AnimeSerializer(serializers.ModelSerializer):
    class Meta:
        model=Anime
        fields=('name','description','image_link','anime_link')

class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model=Genre
        fields=('name','description')

class GenreAnimeSerializer(serializers.ModelSerializer):
    class Meta:
        model=GenreAnime
        fields=('anime', 'genre')