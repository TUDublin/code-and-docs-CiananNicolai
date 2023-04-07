from django.contrib import admin
from .models import Profile

class ProfileAdmin(admin.ModelAdmin):
    list_display = ['username','bio','location']

admin.site.register(Profile, ProfileAdmin)