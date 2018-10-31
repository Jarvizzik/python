#pytest --cov
from playlist.models import Song
from django.test import TestCase
from django.urls import reverse
import playlist.views
import pytest


# If your tests need to use the database and want to use pytest
# function test approach, you need to `mark` it.
@pytest.mark.django_db
class SongTest(TestCase):
    def test_song_unicode(self):
        song = Song(name="Hello", author="Adelle")
        song.save()
        assert song.name == "Hello"
        assert song.author == "Adelle"
        assert song.__unicode__() == song.name
    def test__str__(self):
        song = Song(name="Hello", author="Adelle",adder="adder1")
        song.save()
        assert "Adelle, adder1" == song.__str__()
    def test_index(self):
         # Get the client
        response = self.client.get(reverse('index'))
         # Check the status code
        assert response.status_code == 200
        
    def test_start(self):
         # Get the client
        response = self.client.get(reverse('start'))
         # Check the status code
        assert response.status_code == 200
    def test_register(self):
         # Get the client
        response = self.client.get(reverse('register'))
         # Check the status code
        assert response.status_code == 200


    

