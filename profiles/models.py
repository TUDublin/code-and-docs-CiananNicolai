import uuid
from accounts.models import CustomUser
from django.db import models
from django.urls import reverse
from django.conf import settings
from django.contrib.auth import get_user_model
from django.shortcuts import redirect

class Profile(models.Model):
    username = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    bio = models.TextField(max_length=300, blank=True)
    location = models.CharField(max_length=30, blank=True)

    def __str__(self):
        return self.username