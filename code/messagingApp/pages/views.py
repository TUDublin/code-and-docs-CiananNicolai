from django.views.generic import TemplateView
from django.http import HttpResponse
from django.shortcuts import render

def get_ip_address(request):
    user_ip_address = request.META.get('HTTP_X_FORWARDED_FOR')
    if user_ip_address:
        ip = user_ip_address.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip
def show_ip_address(request):
    user_ip = get_ip_address(request)
    return render(request, "home.html", {"user_ip":user_ip})

class HomePageView(TemplateView):
    template_name = 'home.html'

