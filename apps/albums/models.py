from datetime import datetime

from django.db import models

# Create your models here.

# 相册
class Album(models.Model):
    topic = models.CharField(max_length=20, verbose_name="主题")
    desc = models.CharField(max_length=50, verbose_name="描述", default="")
    image = models.ImageField(
        upload_to="images/covers/%Y",
        verbose_name="封面",
        default="default.png",
        max_length=100,
    )
    created = models.DateTimeField(default=datetime.now, verbose_name="创建时间")
    # 自动更新
    updated = models.DateTimeField(auto_now=True, verbose_name="更新时间")

    class Meta:
        verbose_name = "相册"
        verbose_name_plural = verbose_name
        ordering = ('-created',)

    def __str__(self):
        return self.topic


# 图片
class Images(models.Model):
    title = models.CharField(max_length=80, default="", verbose_name="标题")
    time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")
    album = models.ForeignKey(Album, verbose_name="所属相册", on_delete=models.CASCADE)
    img = models.ImageField(
        upload_to="images/album/%Y",
        verbose_name="图片",
        default="default.png",
        max_length=100,
    )

    class Meta:
        verbose_name = "图片"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title
