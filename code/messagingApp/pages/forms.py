from django import forms
from .models import UserPost, Comment

class Post(forms.ModelForm):
    class Meta:
        model = UserPost
        fields = ('text', 'image')

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('image', 'comment')