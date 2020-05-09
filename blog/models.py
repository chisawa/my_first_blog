# modelは機能,必要ね道具をdjango からinstall
from django.conf import settings
from django.db import models
from django.utils import timezone

# Modelの作成
class Post(models.Model):
    # objects
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

# Postの機能,投稿
    def publish(self):
        self.published_date = timezone.now()
        self.save()

# 管理画面で投稿の一覧をタイトルで表示
    def __str__(self):
        return self.title