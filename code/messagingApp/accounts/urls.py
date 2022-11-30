from django.urls import path
from pages import views
from .views import signupView, signinView, signoutView

urlpatterns = [
    path('create/', signupView, name='signup'),
    path('signout/', signinView, name='signin'),
    path('signout/', signoutView, name='signout'),
]