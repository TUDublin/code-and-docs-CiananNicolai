from django.contrib import admin
from .models import PostType, UserPost

class PostTypeAdmin(admin.ModelAdmin):
    list_display = ['id','name']

admin.site.register(PostType, PostTypeAdmin)

class UserPostAdmin(admin.ModelAdmin):
    list_display = ['id','posttype','username', 'text', 'image','likes','commentCount','postTime','edited']

admin.site.register(UserPost, UserPostAdmin)