from django.contrib import admin
from .models import UserPost, PostType

class PostTypeAdmin(admin.ModelAdmin):
    list_display = ['name']

admin.site.register(PostType, PostTypeAdmin)

class UserPost(admin.ModelAdmin):
    list_display = ['text', 'image']

admin.site.register(UserType, UserPostAdmin)