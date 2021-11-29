from django.db import models
from annoying.fields import AutoOneToOneField
# Create your models here.

class Music(models.Model):
    #location= OneToOneField(Location, on_delete=models.CASCADE)
    title= models.TextField()
    artist= models.TextField()
    audio_file = models.FileField()

    def __str__(self):
        return self.title

class Location(models.Model):
    song = AutoOneToOneField(Music, related_name="location", on_delete=models.CASCADE)
    name=models.TextField()
    longitude= models.DecimalField(max_digits=6, decimal_places=3)
    latitude = models.DecimalField(max_digits=5, decimal_places=3)
