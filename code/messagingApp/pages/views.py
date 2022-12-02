from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, TemplateView
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import UserPost
from django.shortcuts import render,redirect



class HomePageView(TemplateView):
    template_name = 'base.html' 

class PostListView(LoginRequiredMixin, ListView):
    model = UserPost
    template_name = 'post_list.html'

class PostDetailView(LoginRequiredMixin, DetailView):
    model = UserPost
    template_name = 'post_detail.html'

class PostUpdateView(LoginRequiredMixin,UserPassesTestMixin, UpdateView):
    model = UserPost
    fields = ('title', 'body',)
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

