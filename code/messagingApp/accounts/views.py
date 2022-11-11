from django.shortcuts import render
from .forms import CustomUserCreationForm
from .models import CustomUser
from django.contrib.auth.models import Group

def signupView(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            signup_user = CustomUser.objects.get(name='Customer')
            customer_group.user_set.add(signup_user)
    else:
        form = CustomUserCreationForm()
    return render(request, 'signup.html',{'form':form})

# Create your views here.
