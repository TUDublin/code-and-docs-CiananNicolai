from django.views.generic import TemplateView
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import UserPost
from .forms import UserPostForm
from django.http import HttpResponseRedirect



class HomePageView(TemplateView):
    template_name = 'base.html' 

