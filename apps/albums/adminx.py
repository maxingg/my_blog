import xadmin
from albums.models import Album, Images

__author__ = 'maxing'
__date__ = '2018/11/20 10:49'


class AlbumAdmin(object):

    list_display = ['topic', 'image', 'created', 'updated']
    search_fields = ['topic']
    list_filter = ['topic', 'created']


class ImagesAdmin(object):

    list_display = ['id', 'album']
    search_fields = ['album']
    list_filter = ['album']
    model_icon = 'fa fa-picture-o'


xadmin.site.register(Album, AlbumAdmin)
xadmin.site.register(Images, ImagesAdmin)