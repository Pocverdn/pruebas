from django.db import models

# Create your models here.

class filt(models.Model):
    num_events = models.IntegerField()
    genre_music = models.CharField(max_length=200)
    num_musics = models.IntegerField()
    location = models.CharField(max_length=200)

    def __str__(self):
        return self.genre_music
