from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from apiApp.models import Anime, Genre, GenreAnime
from apiApp.serializers import AnimeSerializer, GenreAnimeSerializer, GenreSerializer

@api_view(['GET'])
def getData(request):
    anime = Anime.objects.all()
    print(len(anime))
    serializer = AnimeSerializer(anime, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getAllGenre(request):
    anime = Genre.objects.all()
    serializer = GenreSerializer(anime, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def pushAnime(request):
    serializer = AnimeSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    
@api_view(['POST'])
def pushGenre(request):
    serializer = GenreSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)

@api_view(['POST'])
def pushAnimeGenre(request):
    serializer = GenreAnimeSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
@api_view(['GET'])
def getGenre(request, anime_name):
    genre = GenreAnime.objects.filter(anime = anime_name)
    serializer = GenreAnimeSerializer(genre, many=True)
    return Response(serializer.data)