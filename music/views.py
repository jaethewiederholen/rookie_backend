from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.response import Response
from music.models import Music
from music.serializers import MusicSerializer
from rest_framework.decorators import api_view
from rest_framework.status import HTTP_200_OK, HTTP_204_NO_CONTENT
from django.core.exceptions import ObjectDoesNotExist
# Create your views here.

@api_view(['GET'])
def get_music(request):
    if request.method=="GET":
        lat = request.GET.get('latitude')
        long = request.GET.get('longitude')
        try:
            music= Music.objects.get(location__latitude=lat, location__longitude=long)
        except ObjectDoesNotExist:
            return Response(status=HTTP_204_NO_CONTENT, data={'error': "no content"})
        return Response(status=HTTP_200_OK, data=MusicSerializer(music).data)

@api_view(['GET'])
def get_all_music(request):
    if request.method=="GET":
        return Response(status=HTTP_200_OK, data={"music_list" : MusicSerializer(Music.objects.all(), many=True).data})