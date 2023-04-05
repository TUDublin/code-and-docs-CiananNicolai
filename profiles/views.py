from django.shortcuts import render, get_object_or_404
from .models import Profile
from accounts.models import CustomUser


def profile_context_processor(request):
    profile = None
    if request.user.is_authenticated:
        try:
            profile = Profile.objects.get(username=request.user)
        except Profile.DoesNotExist:
            pass
    return {'profile': profile}

def profile_view(request, username):
    user = get_object_or_404(CustomUser, username=username)
    profile = get_object_or_404(Profile, username=username)
    context = {'profile': profile}
    return render(request, 'profiles/profile.html', context)

def user_profile_view(request, username):
    user = get_object_or_404(CustomUser, username=username)
    profile = Profile.objects.get(user=user)
    context = {'user': user, 'profile': profile}
    return render(request, 'profile.html', context)