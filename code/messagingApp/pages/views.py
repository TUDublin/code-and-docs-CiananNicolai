from django.views.generic import TemplateView
from django.http import HttpResponse
from django.shortcuts import render


class HomePageView(TemplateView):
    template_name = 'base.html'

