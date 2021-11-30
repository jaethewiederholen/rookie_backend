from rest_framework import serializers
from music.models import Music, Location

class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model= Location
        fields =["name", "latitude", "longitude"]

class MusicSerializer(serializers.ModelSerializer):
    _location = LocationSerializer(source="location", read_only=True)
    class Meta:
        model = Music
        fields = ['title', "artist", 'audio_file','_location']