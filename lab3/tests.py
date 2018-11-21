#coverage run manage.py test playlist -v 2
#coverage html
from django.test import TestCase,Client
from playlist.models import Song
import playlist.views
from django.utils import timezone
from django.urls import reverse
from django.contrib.auth.forms import UserCreationForm

class SongTest(TestCase):
    def create_song(self,name="name1",author="author1",adder="adder1"):
        return Song.objects.create(name=name,
                                   author=author,
                                   adder=adder,
                                   added_at = timezone.now(),
                                   updated_at = timezone.now())
    def test_song_creation(self):
        song = self.create_song()
        self.assertTrue(isinstance(song, Song))
        self.assertEqual(song.__unicode__(), song.name)
    def test__str__(self):
        song = self.create_song()
        self.assertEqual("author1, adder1",song.__str__())
        
    def test_index(self):
         # Get the client
        response = self.client.get(reverse('index'))
         # Check the status code
        self.assertEqual(response.status_code, 200)
        
    def test_start(self):
         # Get the client
        response = self.client.get(reverse('start'))
         # Check the status code
        self.assertEqual(response.status_code, 200)
    def test_register(self):
         # Get the client
        response = self.client.get(reverse('register'))
         # Check the status code
        self.assertEqual(response.status_code, 200)
    

