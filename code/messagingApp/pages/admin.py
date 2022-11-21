from django.contrib import admin
from .models import PostType, UserPost

class PostTypeAdmin(admin.ModelAdmin):
    list_display = ['name']

admin.site.register(PostType, PostTypeAdmin)

class UserPostAdmin(admin.ModelAdmin):
    list_display = ['posttype','username', 'text', 'image','likes','comments','edited']

admin.site.register(UserPost, UserPostAdmin)