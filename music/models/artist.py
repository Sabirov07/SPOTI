from django.db import models

class Artist(models.Model):
    name = models.CharField(max_length=200, null=False, blank=False)
    img = models.URLField(blank=True, null=True) # None

    def __str__(self):
        return self.name

