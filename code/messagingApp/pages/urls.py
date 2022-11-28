from django.urls import path
from .views import (
    PostListView,
    PostUpdateView,
    PostDetailView,
    PostDeleteView,
    PostCreateView,
    CommentCreateView,
    HomePageView,
)


urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('<uuid:pk>/edit/',
        PostUpdateView.as_view(), name='post_edit'),

    path('<uuid:pk>',
        PostDetailView.as_view(), name='post_detail'),

    path('comment/',
        CommentCreateView.as_view(), name='post_comment'),

    path('<uuid:pk>/delete/',
        PostDeleteView.as_view(), name='post_delete'),

    path('new/', PostCreateView.as_view(), name='post_new'),
    path('', PostListView.as_view(), name='post_list'),
    ]