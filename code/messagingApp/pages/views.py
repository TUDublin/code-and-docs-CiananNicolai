from pyexpat import model
from django.views.generic import TemplateView, ListView
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import UserPost
from django.http import HttpResponseRedirect



class HomePageView(TemplateView):
    template_name = 'base.html' 

class UserPostList(ListView):
    model = UserPost
    queryset = UserPost.objects.order_by('-postTime')
    template_name = 'base.html'

