from django.db import models
from .artist import Artist

class Album(models.Model):
    name = models.CharField(max_length=200, blank=False, null=False)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    created_date = models.DateField(auto_now_add=True)


    def __str__(self):
        return self.name

