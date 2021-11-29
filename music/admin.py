from django.contrib import admin
from .models import Music, Location
# Register your models here.

@admin.register(Music)
class MusicAdmin(admin.ModelAdmin):
    list_display= ('title', 'artist', 'audio_file')

@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    list_display= ('song', 'latitude', 'longitude')