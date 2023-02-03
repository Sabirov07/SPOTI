from django.db import models
from .artist import Artist
from .album import Album

class Song(models.Model):
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    title = models.CharField(max_length=200, blank=False, null=False)
    file = models.URLField()

    def __str__(self):
        return self.title