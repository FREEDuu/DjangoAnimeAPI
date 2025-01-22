from django.db import models

class Anime(models.Model):
    name = models.CharField(max_length=200, primary_key=True)
    description = models.CharField(max_length=1000)
    image_link = models.CharField(max_length=300)
    anime_link = models.CharField(max_length=300)

class Genre(models.Model):
    name = models.CharField(max_length=200, primary_key=True)
    description = models.CharField(max_length=1000)

class GenreAnime(models.Model):
    anime = models.ManyToManyField(Anime)
    genre = models.ManyToManyField(Genre)