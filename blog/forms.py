from django import forms
from .models import Post


class PostForm(forms.Form):
    title = forms.CharField()
    #text=forms.CharField()
    text = forms.CharField(widget=forms.Textarea)

    # class Meta:
    #     model = Post
    #     fields = ('title', 'text',)