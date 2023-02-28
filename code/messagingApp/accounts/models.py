from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    age = models.PositiveBigIntegerField(null=True, blank=True)
    avatar = models.ImageField(default='placeholder.jpg', blank=True, upload_to='media/profile_images')
    latitude = models.DecimalField(max_digits=9, decimal_places=6)
    longitude = models.DecimalField(max_digits=9, decimal_places=6)
    