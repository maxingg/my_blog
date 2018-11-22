from django.shortcuts import render, redirect

# Create your views here.
from django.views import View


class BlogBaseView(View):
    def get(self, request):
        return render(request, 'blog_base.html', locals())


class BlogUserInfoView(View):
    def get(self, request):
        res = 'user' in request.path
        if res:
            name = 'user'
        else:
            name = ''
        return render(request, 'blog_userinfo.html', locals())


class XadminView(View):
    def get(self, request):
        return redirect(request, 'xadmin/')
