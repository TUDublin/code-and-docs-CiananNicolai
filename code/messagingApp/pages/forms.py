from django import forms
from .models import UserPost

class ImageForm(forms.ModelForm):
    class Meta:
        model = UserPost
        fields = ('text', 'image')

