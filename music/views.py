from django.contrib.postgres.search import TrigramSimilarity
from django.shortcuts import render
from rest_framework import views, permissions, filters
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status
from rest_framework.viewsets import ModelViewSet
from django.db import transaction

from .models.artist import Artist
from .serializer import ArtistSerializer

from .models.album import Album
from .serializer import AlbumSerializer

from .models.song import Song
from .serializer import SongSerializer

class ArtistAPIViewSet(ModelViewSet):
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer

    @action(detail=True, methods=['GET'])
    def albums(self, request, *args, **kwargs):
        artist = self.get_object()
        serializer = AlbumSerializer(artist.album_set.all(), many=True)
        return Response(serializer.data)
    @action(detail=True, methods=['GET'])
    def songs(self, request, *args, **kwargs):
        artist = self.get_object()
        serializer = SongSerializer(artist.song_set.all(), many=True)
        return Response(serializer.data)

class AlbumAPIViewSet(ModelViewSet):
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer
    @action(detail=True, methods=['GET'])
    def songs(self, request, *args, **kwargs):
        album =self.get_object()
        serializer =SongSerializer(album.song_set.all(), many=True)
        return Response(serializer.data)




#CRUD -> Create-Update-Retrieve-Delete
class SongApiViewSet(ModelViewSet):
    queryset =Song.objects.all()
    serializer_class =SongSerializer
    permission_classes = [permissions.AllowAny]
    # filter_backends = [filters.SearchFilter]
    # search_fields = ["title"]

    def get_queryset(self):
        queryset = Song.objects.all()
        query = self.request.query_params.get('search')
        if query is not None:
            queryset = Song.objects.annotate(similarity=TrigramSimilarity('title', query)).filter(similarity__gt=0.2)
        return queryset

# postgresql -> TrigramSimilarity


