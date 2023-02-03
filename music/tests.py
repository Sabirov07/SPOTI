from django.test import TestCase
from .models import Artist
from .models import Album

class AnimalTestCase(TestCase):
    def setUp(self):
        artist1 = Artist.objects.create(name="Billie")
        album = Album.objects.create(name="First album", artist=artist1)

    def album_test(self):

        album = Album.objects.get(name="First album")
        self.assertEqual(album)

# class AlbumTestCase(TestCase):
    # def setUp(self):
    #     artist1 = Artist.objects.create(name="Billie")
    #     album = Album.objects.create(name="First album", artist=artist1)
    #
    #
    # # def album(self):
    # #     assert True
