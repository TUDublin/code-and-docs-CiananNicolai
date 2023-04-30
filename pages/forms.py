from django import forms
from .models import UserPost, Comment

class UserPostForm(forms.ModelForm):
    use_geo = forms.BooleanField(initial=True, widget=forms.HiddenInput(), required=False)

    class Meta:
        model = UserPost
        fields = ('text', 'image', 'latitude', 'longitude', 'posttype')
        widgets = {
            'latitude': forms.HiddenInput(),
            'longitude': forms.HiddenInput(),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.initial['posttype'] = 'userpost'


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
        exclude = ( 'post', 'author', 'likes', 'postTime', 'edited', 'status',)
    
    def __init__(self, *args, **kwargs):
        self.post = kwargs.pop('post')
        self.author = kwargs.pop('author')
        super().__init__(*args, **kwargs)

    def save(self, commit=True):
        instance = super().save(commit=False)
        instance.post = self.post
        instance.author = self.author
        instance.id = self.post.id
        if commit:
            instance.save()
        return instance