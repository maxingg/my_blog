"""my_blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls.static import static
from django.urls import path, re_path, include
from django.views.static import serve
import xadmin
from my_blog import settings
from user.views import *
from music.views import *

from my_blog.settings import MEDIA_ROOT

urlpatterns = [
    path('xadmin/', xadmin.site.urls),
    path('xadmin/', XadminView.as_view(), name="xadmin"),
    path('', BlogBaseView.as_view(), name="home"),

    path('mdeditor/', include('mdeditor.urls')),
    path('albums/', include('albums.urls', namespace="albums")),
    path('articles/', include('articles.urls', namespace="articles")),
    path('user', include('user.urls', namespace="user")),
    path('music/', include('music.urls', namespace="music")),

    re_path('media/(?P<path>.*)', serve, {'document_root': MEDIA_ROOT}),
]

if settings.DEBUG:
    # static files (images, css, javascript, etc.)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
