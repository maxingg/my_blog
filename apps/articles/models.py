from datetime import datetime

from django.db import models
from mdeditor.fields import MDTextField

from user.models import UserProfile


class Article(models.Model):
    TAG_CHOICES = (
        ('C++', 'C++'),
        ('Java', 'Java'),
        ('Python', 'Python'),
        ('Kaggle', 'Kaggle'),
    )
    author = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    title = models.CharField(max_length=50, verbose_name="标题")
    subtitle = models.CharField(max_length=50, default="", verbose_name="副标题")
    tag = models.CharField(choices=TAG_CHOICES, max_length=20, verbose_name="文章类型", default="python")
    desc = models.CharField(max_length=100, verbose_name="描述", default="")
    # 大量文本保存使用TextField
    body = MDTextField()
    created = models.DateTimeField(default=datetime.now)
    updated = models.DateTimeField(auto_now=True)
    image = models.ImageField(
        upload_to="images/articles/%Y",
        verbose_name="文章封面",
        default="default.png",
        max_length=100,
    )

    class Meta:
        verbose_name = "文章"
        verbose_name_plural = verbose_name
        ordering = ('-created',)

    def __str__(self):
        return self.title
