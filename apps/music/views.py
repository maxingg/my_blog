from django.shortcuts import render

# Create your views here.
from django.views import View


class BlogMusicView(View):
    def get(self, request):
        res = 'music' in request.path
        if res:
            name = 'music'
        else:
            name = ''
        return render(request, 'blog_music.html', locals())
