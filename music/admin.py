from django.contrib import admin
from .models import artist
from .models import album
from .models import song

admin.site.register(album.Album),
admin.site.register(artist.Artist),
admin.site.register(song.Song),