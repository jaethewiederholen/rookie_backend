from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from . import views

app_name = "music"

urlpatterns = [
    path('get-music', views.get_music),
    path('get-all-music', views.get_all_music),
]