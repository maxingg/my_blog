import markdown
from django.http import HttpResponse
from django.shortcuts import render, redirect
from pure_pagination import Paginator, EmptyPage, PageNotAnInteger
from django.views import View

from articles.forms import ArticleForm
from articles.models import Article
from user.models import UserProfile


class BlogArticlesView(View):
    def get(self, request):
        res = 'articles' in request.path
        if res:
            name = 'articles'
        else:
            name = ''

        # 课程筛选
        filter = request.GET.get('filter', "")
        if filter:
            all_articles = Article.objects.filter(tag__icontains=filter)
        else:
            all_articles = Article.objects.all()

        if all_articles:
            articles_nums = all_articles.count()
        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1
        p = Paginator(all_articles, 4, request=request)
        all_articles = p.page(page)
        return render(request, 'blog_articles.html', locals())


class ArticleDetailView(View):
    def get(self, request, article_id):
        article = Article.objects.get(id=article_id)

        article.body = markdown.markdown(article.body,
                                         extensions=[
                                             # 包含 缩写、表格等常用扩展
                                             'markdown.extensions.extra',
                                             # 语法高亮扩展
                                             'markdown.extensions.codehilite',
                                             'markdown.extensions.toc',
                                         ])
        context = {'article': article}
        return render(request, 'article_detail.html', locals())


