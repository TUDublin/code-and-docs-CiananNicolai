from django.urls import path
from views import view_profile

urlpatterns = [
    path('profile/<str:username>/', view_profile, name='view_profile'),

]