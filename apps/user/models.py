from django.contrib.auth.models import AbstractUser

from django.db import models

__author__ = 'maxing'
__date__ = '2018/11/20 18:57'


class UserProfile(AbstractUser):

    GENDER_CHOICES = (
        ("male", "男"),
        ("female", "女"),
    )
    # 昵称
    nick_name = models.CharField(max_length=50, verbose_name="昵称", default="")
    # 生日 可以为空
    birthday = models.DateField(verbose_name="生日", null=True, blank=True)
    hobby = models.CharField(default='', max_length=80, verbose_name='爱好')
    # 性别
    gender = models.CharField(
        max_length=6,
        choices=GENDER_CHOICES,
        default="male",
        verbose_name="性别",
    )
    # 地址
    address = models.CharField(max_length=100, verbose_name="地址", default="")
    # 电话
    mobile = models.CharField(max_length=11, null=True, blank=True)
    # 头像 默认用default.png
    image = models.ImageField(
        upload_to="images/portraits/%Y",
        default="default.png",
        max_length=100,
    )

    # meta信息，后台栏目名
    class Meta:
        verbose_name = "用户信息"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.username