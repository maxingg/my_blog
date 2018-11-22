__author__ = 'maxing'
__date__ = '2018/11/20 13:02'

from django.urls import path

from .views import BlogMusicView

app_name = 'music'

urlpatterns = [
    path('play/', BlogMusicView.as_view(), name="music_play"),
]
