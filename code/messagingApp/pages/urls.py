from django.urls import path
from . import views
from .views import (
    PostUpdateView,
    PostDetailView,
    PostDeleteView,
    PostCreateView,
    HomePageView,
    CommentCreateView,
)

app_name = "pages"

urlpatterns = [
    path('home/', HomePageView.as_view(), name='home'),
    path('<uuid:pk>/edit/',
        PostUpdateView.as_view(), name='post_edit'),

    path('<uuid:pk>',
        PostDetailView.as_view(), name='post_detail'),

    path('<uuid:pk>/delete/',
        PostDeleteView.as_view(), name='post_delete'),

    path('new/', PostCreateView.as_view(), name='post_new'),
    path('history', views.postHistory, name='post_history'),
    path('comment/',CommentCreateView.as_view(), name='comment_detail'),
    ]