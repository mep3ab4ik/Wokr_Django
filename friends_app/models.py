from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Friends(models.Model):
    friend = models.ManyToManyField(User, blank=True, related_name='friends')
    date = models.DateTimeField(auto_now_add=True)


class Subscribe(models.Model):
    sub = models.ManyToManyField(User, blank=True, related_name='subscribe')
    date = models.DateTimeField(auto_now_add=True)