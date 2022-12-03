from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, TemplateView
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import UserPost, CustomUser, Comment
from django.shortcuts import render,redirect, get_object_or_404
from .forms import CommentForm


class HomePageView(TemplateView):
    template_name = 'base.html' 

class CommentCreateView(LoginRequiredMixin, CreateView):
    model = Comment
    fields = ('image', 'comment')
    template_name = 'comment_detail.html'
    success_url = reverse_lazy('post_list')

    def form_valid(self, form):
        form.instance.username = self.request.user
        return super().form_valid(form)


def postHistory(request):
    post_details = UserPost.objects.all
    return render(request,'post_list.html',{'post_details': post_details})

class PostDetailView(LoginRequiredMixin, DetailView):
    model = UserPost
    template_name = 'post_detail.html'

class PostUpdateView(LoginRequiredMixin,UserPassesTestMixin, UpdateView):
    model = UserPost
    fields = ('image', 'text',)
    template_name = 'post_edit.html'

    def test_func(self):
        obj = self.get_object()
        return obj.username == self.request.user

class PostDeleteView(LoginRequiredMixin,UserPassesTestMixin, DeleteView):
    model = UserPost
    template_name = 'post_delete.html'
    success_url = reverse_lazy('post_list')

    def test_func(self):
        obj = self.get_object()
        return obj.username == self.request.user

class PostCreateView(LoginRequiredMixin, CreateView):
    model = UserPost
    fields = ('username', 'text', 'image')
    template_name = 'post_new.html'

    def form_valid(self, form):
        form.instance.username = self.request.user
        return super().form_valid(form)

def viewPost(request, comment_id):
    if request.user.is_authenticated:
        posts = UserPost.objects.get(id=comment_id)
        post_items = Comment.objects.all
    return render(request, 'post/post_detail.html', {'post':posts, 'post_items':post_items})