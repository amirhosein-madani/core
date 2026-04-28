from django import forms
from .models import Post


class PostFOrm(forms.Form):

    class Meta:
        model = Post
        fields = ["title", "content", "status", "published_date"]
