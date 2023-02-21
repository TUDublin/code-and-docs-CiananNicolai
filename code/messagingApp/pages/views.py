from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, TemplateView
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import UserPost, CustomUser, Comment
from django.shortcuts import render,redirect, get_object_or_404, HttpResponse
from .forms import CommentForm
from django.contrib.gis.geoip2 import GeoIP2


class HomePageView(TemplateView):
    template_name = 'home.html' 

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
    success_url = reverse_lazy('pages:post_history')

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

class CommentCreateView(LoginRequiredMixin, CreateView):
    model = Comment
    fields = ('image', 'comment')
    template_name = 'comment_detail.html'
    success_url = reverse_lazy('pages:post_history')

    def form_valid(self, form):
        form.instance.username = self.request.user
        return super().form_valid(form)

def postComment(request):
     comments = comments.all()

def home(request):
    print("test")
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')    
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    
    device_type = ""
    browser_type = ""
    browser_version = ""
    os_type = ""
    os_version = ""    
    if request.user_agent.is_mobile:
        device_type = "Mobile"
    if request.user_agent.is_tablet:
        device_type = "Tablet"
    if request.user_agent.is_pc:
        device_type = "PC"
    
    browser_type = request.user_agent.browser.family
    browser_version = request.user_agent.browser.version_string
    os_type = request.user_agent.os.family
    os_version = request.user_agent.os.version_string
    
    g = GeoIP2()
    location = g.city(ip)
    location_country = location["country_name"]
    location_city = location["city"]    
    context = {
        "ip": ip,
        "device_type": device_type,
        "browser_type": browser_type,
        "browser_version": browser_version,
        "os_type":os_type,
        "os_version":os_version,
        "location_country": location_country,
        "location_city": location_city
    }
    
    return render(request, "signin.html", context)