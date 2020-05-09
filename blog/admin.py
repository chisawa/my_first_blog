from django.contrib import admin
# models.pyで作ったPostを使う
from .models import Post

# Postモデルを登録
admin.site.register(Post)

# Register your models here.
