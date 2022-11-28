from django.urls import path
from .views import HomePageView, UserPostList


urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('', UserPostList.as_view(), name='home'),
    ]