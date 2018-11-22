__author__ = 'maxing'
__date__ = '2018/11/20 13:02'

from django.urls import path, include, re_path

from .views import BlogAlbumsView, AlbumContentView

app_name = 'albums'

urlpatterns = [
    path('albums_wall/', BlogAlbumsView.as_view(), name="albums_wall"),
    re_path('album_content/(?P<album_id>\d+)/', AlbumContentView.as_view(), name="album_content"),

]
