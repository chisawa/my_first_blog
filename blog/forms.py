# modelをさらに細く設定
from django import forms
from .models import Post

# djangoのformsからModelFormを使う
class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        # Postモデルのうち自分で記述する必要のある項目
        fields = ('title', 'text',)