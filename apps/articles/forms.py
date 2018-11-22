__author__ = 'maxing'
__date__ = '2018/11/20 9:30'

from django import forms
from .models import Article

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ('title', 'body')