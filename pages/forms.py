from django import forms
from .models import UserPost, Comment

class UserPostForm(forms.ModelForm):
    class Meta:
        model = UserPost
        fields = ('text', 'image', 'latitude', 'longitude','posttype')
        widgets = {
            'latitude': forms.HiddenInput(),
            'longitude': forms.HiddenInput(),
        }

class UserPostFormWithLocation(UserPostForm):
    use_geo = forms.BooleanField(required=False)

    class Meta(UserPostForm.Meta):
        fields = UserPostForm.Meta.fields + ('use_geo',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['latitude'].required = False
        self.fields['longitude'].required = False
        
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('image', 'comment')