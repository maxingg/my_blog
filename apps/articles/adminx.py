import xadmin

from articles.models import Article

__author__ = 'maxing'
__date__ = '2018/11/20 10:51'


class ArticleAdmin(object):

    list_display = ['title', 'author', 'created', 'updated']
    search_fields = ['author', 'created']
    list_filter = ['author', 'created']
    model_icon = 'fa fa-book'



xadmin.site.register(Article, ArticleAdmin)