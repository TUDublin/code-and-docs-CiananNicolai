from django.urls import path
from .views import HomePageView, show_ip_address
from pages.views import show_ip_address


urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('user_ip/',show_ip_address),
    ]