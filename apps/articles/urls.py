__author__ = 'maxing'
__date__ = '2018/11/20 13:02'

from django.urls import path, include, re_path

from .views import BlogArticlesView, ArticleDetailView

app_name = 'articles'

urlpatterns = [
    path('articles-list/', BlogArticlesView.as_view(), name="articles_list"),

    re_path('article_detail/(?P<article_id>\d+)/', ArticleDetailView.as_view(), name="article_detail"),
]
