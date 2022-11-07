import uuid
from django.db import models
from django.urls import reverse


class PostType(models.Model):
        id = models.UUIDField(
        primary_key=True
        default=uuid.uuid4
        editable=False
    )
    name = models.CharField(max_length=250, unique=True)

    class Meta:
        ordering =('name',)
        verbose_name = 'type'
        verbose_name_plural ="types"
    
    def get_absolute_url(self):
        return reverse('pages:posts_by_type', args=[self.id])

    def __str__(self):
        return self.name


class UserPost(models.Model):
    id = models.UUIDField(
        primary_key=True
        default=uuid.uuid4
        editable=False
    )
    text = models.CharField(max_length=250, unique=True)
    image = models.ImageField(upload_to="userPost", blank=True)
    likes = models.DecimalField(black=True)
    comments = models.DecimalField(black=True)
    postTime = models.DateTimeField(auto_now_add=True, black=True, null=True)
    edited = models.DateTimeField(auto_now_add=True, black=True, null=True)

    class Meta:
        ordering =('text',)
        verbose_name = 'post'
        verbose_name_plural ="posts"
    
    def get_absolute_url(self):
        return reverse('pages:post detail', args=[self.posttype.id, self.id])

    def __str__(self):
        return self.name