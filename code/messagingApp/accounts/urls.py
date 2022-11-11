from django.urls import path
from .views import signupView

urlpatterns = [
    path('create/', signupView, name='signup')
]