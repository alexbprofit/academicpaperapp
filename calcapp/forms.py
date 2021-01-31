from django import forms

from .models import Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('param1', 'param2', 'param3', 'epsilon', 'nums',)
