__author__ = 'maxing'
__date__ = '2018/11/20 13:01'
from django.urls import path

from .views import BlogUserInfoView

app_name = 'user'

urlpatterns = [
    path('user_info', BlogUserInfoView.as_view(), name="userinfo"),
]
