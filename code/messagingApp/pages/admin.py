from django.contrib import admin
from .models import PostType, UserPost

class PostTypeAdmin(admin.ModelAdmin):
    list_display = ['name']

admin.site.register(PostType, PostTypeAdmin)

class UserPostAdmin(admin.ModelAdmin):
    list_display = ['posttype', 'text', 'image','likes','comments','postType','edited']

admin.site.register(UserType, UserPostAdmin)