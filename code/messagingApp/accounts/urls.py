from django.urls import path
from .views import signupView, signinView

urlpatterns = [
    path('create/', signupView, name='signup'),
    path('login/', signupView, name='signin')
]