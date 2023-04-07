from django.shortcuts import render, get_object_or_404
from .models import Profile
from accounts.models import CustomUser
from django.contrib.auth import get_user_model


from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth import get_user_model
from .models import Profile
from pages.models import UserPost

@receiver(post_save, sender=get_user_model())
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(username=instance)

def profile_view(request, username):
    User = get_user_model()
    user = get_object_or_404(User, username=username)
    profile = get_object_or_404(Profile, username_id=user)
    post_list = UserPost.objects.filter(username=user)
    context = {'user': user, 'profile': profile, 'post_list': post_list}
    return render(request, 'profile.html', context)

