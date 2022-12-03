import uuid
from accounts.models import CustomUser
from django.db import models
from django.urls import reverse
from django.conf import settings
from django.contrib.auth import get_user_model


class PostType(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default= uuid.uuid4,
        editable=True),
    name = models.CharField(max_length=250, unique=True)

    class Meta:
        ordering =('name',)
        verbose_name = 'type'
        verbose_name_plural ="types"
    
    def get_absolute_url(self):
        return reverse('post_detail', args=[str(self.id)])

    def __str__(self):
        return self.name

STATUS = (
    (0,"Draft"),
    (1,"Publish")
)

class UserPost(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )
    posttype = models.ForeignKey(PostType, on_delete=models.CASCADE)
    username = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    text = models.TextField(max_length=250)
    image = models.ImageField(upload_to="userPost", blank=True)
    likes = models.DecimalField(blank=True,max_digits=9999999,decimal_places=0, null=True)
    commentCount = models.DecimalField(blank=True,max_digits=9999999,decimal_places=0, null=True)
    postTime = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    edited = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    status = models.IntegerField(choices=STATUS, default=0)


    class Meta:
        ordering =('-postTime',)
        verbose_name = 'userpost'
        verbose_name_plural ="userposts"
    
    def get_absolute_url(self):
        return reverse('post_detail', args=[str(self.id)])
    def __str__(self):
        return self.text


class Comment(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )
    comment = models.TextField(max_length=250)
    image = models.ImageField(upload_to="userPost", blank=True)
    likes = models.DecimalField(blank=True,max_digits=9999999,decimal_places=0, null=True)
    username = models.ForeignKey(get_user_model(),on_delete = models.CASCADE)
    postTime = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    edited = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    status = models.IntegerField(choices=STATUS, default=0)

    def str(self):
        return self.comment

    def get_absolute_url(self):
        return reverse('post_detail', args=[str(self.part.id)])