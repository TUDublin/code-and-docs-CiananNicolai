import uuid
from accounts.models import CustomUser
from django.db import models
from django.urls import reverse
from django.conf import settings


class PostType(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default= uuid.uuid4,
        editable=False),
    name = models.CharField(max_length=250, unique=True)

    class Meta:
        ordering =('name',)
        verbose_name = 'type'
        verbose_name_plural ="types"
    
    def get_absolute_url(self):
        return reverse('pages:posts_by_type', args=[self.id])

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
    text = models.CharField(max_length=250, unique=True)
    image = models.ImageField(upload_to="userPost", blank=True)
    likes = models.DecimalField(blank=True,max_digits=9999999,decimal_places=0)
    comments = models.CharField(blank=True, max_length=250)
    postTime = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    edited = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    status = models.IntegerField(choices=STATUS, default=0)


    class Meta:
        ordering =('-postTime',)
        verbose_name = 'userpost'
        verbose_name_plural ="userposts"
    
    def get_absolute_url(self):
        return reverse('pages', args=[self.id])

    def __str__(self):
        return self.username