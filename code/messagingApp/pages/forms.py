from django import forms
from .models import UserPost

class Post(forms.ModelForm):
    class Meta:
        model = UserPost
        fields = ('text', 'image')

