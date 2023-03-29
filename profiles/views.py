from django.shortcuts import render, get_object_or_404
from .models import Profile
from accounts.models import CustomUser


def view_profile(request, username):
    user = get_object_or_404(CustomUser, username=username)
    profile = get_object_or_404(Profile, user=user)
    return render(request, 'profiles/view_profile.html', {'profile': profile})