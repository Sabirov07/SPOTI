from rest_framework import serializers
from .models import album, artist, song
import datetime

class ArtistSerializer(serializers.ModelSerializer):
    class Meta:
        fields = "__all__"
        model = artist.Artist

class AlbumSerializer(serializers.ModelSerializer):
    class Meta:
        fields = "__all__"
        model = album.Album


    #TODO: created_date keyin buyunki date bn solishtramiz...
    #def validate(self, attrs):
        #print(datetime.datetime.now())
       # if attrs['created_date'].endswith(datetime.datetime.now()):
          #  return attrs
     #   raise serializers.ValidationError('this is out of date')


class SongSerializer(serializers.ModelSerializer):
    class Meta:
        fields = "__all__"
        model = song.Song

    def validate(self, attrs):
        if attrs['file'].endswith('.mp3'):
            return attrs
        raise serializers.ValidationError('File must be mp3')