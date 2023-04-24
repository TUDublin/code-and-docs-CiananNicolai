from django.contrib import admin
from .models import PostType, UserPost, Comment

class PostTypeAdmin(admin.ModelAdmin):
    list_display = ['id','name']

admin.site.register(PostType, PostTypeAdmin)

class UserPostAdmin(admin.ModelAdmin):
    list_display = ['id','posttype','username', 'text', 'image','likes','commentCount','postTime','edited', 'latitude','longitude']
    list_editable = ['latitude','longitude']

admin.site.register(UserPost, UserPostAdmin)

class CommentAdmin(admin.ModelAdmin):
    list_display = ['id','author', 'comment', 'image','likes','postTime','edited']

admin.site.register(Comment, CommentAdmin)