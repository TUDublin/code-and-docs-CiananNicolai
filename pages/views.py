from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, TemplateView
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import UserPost, CustomUser, Comment, PostLike
from django.shortcuts import render,redirect, get_object_or_404, reverse, HttpResponse
from .forms import CommentForm, UserPostForm, UserPostFormWithLocation
from django.contrib.gis.geoip2 import GeoIP2
from math import radians, sin, cos, sqrt, atan2
import logging
import urllib.request, json, pandas as pd
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError
from django.contrib import messages
from profiles.models import Profile
from profiles.views import Profile



logger = logging.getLogger(__name__)

class HomePageView(TemplateView):
    template_name = 'home.html' 

# def postHistory(request):
#     post_details = UserPost.objects.all
#     return render(request,'post_list.html',{'post_details': post_details})

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
    form_class = UserPostFormWithLocation
    template_name = 'post_new.html'
    success_url = reverse_lazy('pages:post_history')

    def form_valid(self, form):
        post = form.save(commit=False)
        if form.cleaned_data['use_geo']:
            location = self.get_user_location()
            if location:
                post.latitude, post.longitude = location
            else:
                messages.warning(self.request, 'Could not determine your location.')
        form.instance.username = self.request.user
        post.save()
        return super().form_valid(form)

    def get_user_location(self):
        try:
            position = self.request.GET.get('position', '')
            lat, lng = position.split(',')
            return float(lat), float(lng)
        except Exception as e:
            print(e)
            return None

    def dispatch(self, request, *args, **kwargs):
        if request.GET.get('use_geo') == '1':
            return render(request, 'get_location.html')
        return super().dispatch(request, *args, **kwargs)

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        if self.request.GET.get('use_geo') == '1':
            kwargs['initial'] = {'use_geo': True}
        return kwargs

def viewPost(request, comment_id):
    if request.user.is_authenticated:
        posts = UserPost.objects.get(id=comment_id)
        post_items = Comment.objects.all
    return render(request, 'post/post_detail.html', {'post':posts, 'post_items':post_items})

class CommentCreateView(LoginRequiredMixin, CreateView):
    model = Comment
    fields = ('comment', 'image')
    template_name = 'comment_create.html'
    success_url = reverse_lazy('pages:post_history')

    def form_valid(self, form):
        form.instance.author = self.request.user
        post_id = self.kwargs.get('post_id')
        form.instance.post = UserPost.objects.get(id=post_id)

        return super().form_valid(form)

def postComment():
     comments = comments.all()

class PostDetailView(DetailView):
    model = UserPost
    template_name = 'comment_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        post = self.get_object()
        comments = post.comments.all()
        context['comments'] = comments
        return context



def my_view(request):
    logger.critical("test", request.GET)
    radius = 15 # km
    visible_posts = []
    
    if request.method == 'POST' and 'latitude' in request.POST and 'longitude' in request.POST:
        lat = request.POST['latitude']
        long = request.POST['longitude']
        logger.critical(lat, long)

        # filter posts that are within the desired radius of the user's location
        for post in UserPost.objects.all():
            distance = calculate_distance(lat, long, post.latitude, post.longitude)
            if distance <= radius:
                visible_posts.append(post)

        # create a list of dictionaries containing the visible posts
        data = [{'pk': post.pk,'username': post.username,'text': post.text,'likes': post.likes,'latitude': post.latitude, 'longitude': post.longitude} for post in visible_posts]

        # render the post_list.html template with the visible posts
        return render(request, 'post_list.html', {'post_list': data})

    # return an empty response if the GET parameters are missing
    #return HttpResponse('')

    elif request.method == 'GET':
        # Get the user's IP address
        user_ip = "92.251.255.11"
        url = f'http://ipinfo.io/{user_ip}/json'
        with urllib.request.urlopen(url) as response:
            data = json.loads(response.read().decode())
            logger.critical(data)
        user_latitude, user_longitude = data['loc'].split(',')
        for post in UserPost.objects.all():
            distance = calculate_distance(user_latitude, user_longitude, post.latitude, post.longitude)
            if distance <= radius:
                visible_posts.append(post)

        # create a list of dictionaries containing the visible posts
        data = [{'pk': post.pk,'username': post.username,'text': post.text,'likes': post.likes,'latitude': post.latitude, 'longitude': post.longitude} for post in visible_posts]
        # redirect to the same view with the obtained latitude and longitude as query string parameters
        return render(request, 'post_list.html', {'post_list': data})
    else:
         # handle other HTTP methods
         return HttpResponseNotAllowed(['GET'])
    

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

@login_required
@require_POST
def like_post(request, uuid):
    post = get_object_or_404(UserPost, id=uuid)
    try:
        like = PostLike.objects.create(user=request.user, post=post)
        liked = True
    except IntegrityError:
        # the user has already liked this post
        like = PostLike.objects.get(user=request.user, post=post)
        like.delete()
        liked = False

    post.likes = post.postlike_set.count()
    post.save()

    return redirect(reverse('pages:post_history'))
