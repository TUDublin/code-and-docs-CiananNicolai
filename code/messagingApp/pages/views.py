from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, TemplateView
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import UserPost, CustomUser, Comment
from django.shortcuts import render,redirect, get_object_or_404, HttpResponse
from .forms import CommentForm
from django.contrib.gis.geoip2 import GeoIP2
from math import radians, sin, cos, sqrt, atan2




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
        user_ip = self.request.META.get('REMOTE_ADDR')
        # Use GeoIP2 library to get latitude and longitude coordinates from IP address
        geo = GeoIP2()
        user_location = geo.city(user_ip)
        latitude = user_location['latitude']
        longitude = user_location['longitude']              
        post = form.save(commit=False)
        post.latitude = latitude
        post.longitude = longitude
        post.save()
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

def postComment():
     comments = comments.all()

def showIP(request):
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
    print(context)
    return render(request, "HomePageView", context)

def my_view(request):
    user_ip = request.META.get('REMOTE_ADDR', None)
    response = request.get(f'http://ipinfo.io/{user_ip}/json')
    data = response.json()
    user_latitude, user_longitude = data['loc'].split(',')
    radius = 10 # km
    visible_posts = []

    # filter posts that are within the desired radius of the user's location
    for post in UserPost.objects.all():
        distance = calculate_distance(user_latitude, user_longitude, post.latitude, post.longitude)
        if distance <= radius:
            visible_posts.append(post)

    # render the template with the visible posts
    context = {'posts': visible_posts}
    return render(request, 'post_list.html', context)

def calculate_distance(lat1, lon1, lat2, lon2):
    # approximate radius of Earth in km
    R = 6373.0

    # convert latitude and longitude from degrees to radians
    lat1, lon1, lat2, lon2 = map(radians, [float(lat1), float(lon1), float(lat2), float(lon2)])

    # calculate the difference between the latitudes and longitudes
    dlat = lat2 - lat1
    dlon = lon2 - lon1

    # apply the Haversine formula to calculate the distance between the points
    a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))
    distance = R * c

    return distance