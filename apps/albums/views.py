from django.shortcuts import render

# Create your views here.
from django.views import View
from pure_pagination import Paginator, EmptyPage, PageNotAnInteger
from albums.models import Album, Images


class BlogAlbumsView(View):
    def get(self, request):
        res = 'albums' in request.path
        if res:
            name = 'albums'
        else:
            name = ''
        all_albums = Album.objects.all()
        articles_nums = all_albums.count()
        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1
        p = Paginator(all_albums, 7, request=request)
        all_albums = p.page(page)
        return render(request, 'blog_albums.html', locals())


class AlbumContentView(View):

    def get(self, request, album_id):
        album = Album.objects.get(id=album_id)
        images = Images.objects.filter(album=album)
        return render(request, 'show_images.html', locals())
