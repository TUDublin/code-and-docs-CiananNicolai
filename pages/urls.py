from django.urls import path
from . import views
from .views import (
    PostUpdateView,
    PostDetailView,
    PostDeleteView,
    PostCreateView,
    HomePageView,
    CommentCreateView,
    like_post,
    my_view,
)

app_name = "pages"

urlpatterns = [
    path('home/', 
        HomePageView.as_view(), name='home'),
    path('<uuid:pk>/edit/',
        PostUpdateView.as_view(), name='post_edit'),

    path('<uuid:pk>',
        PostDetailView.as_view(), name='post_detail'),

    path('<uuid:pk>/delete/',
        PostDeleteView.as_view(), name='post_delete'),

    path('new/', PostCreateView.as_view(), name='post_new'),
    path('history/', views.my_view, name='post_history'),
    path('comment/',CommentCreateView.as_view(), name='comment_detail'),
    path('post/<uuid:uuid>/like/', like_post, name='like_post'),
    path('history/', views.my_view, name='my_view'),

    ]

    #views.showIP