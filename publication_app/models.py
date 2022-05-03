from django.contrib.auth.models import User
from django.db import models
# Create your models here.


class Post(models.Model):
    created_time = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=256, unique=False, blank=False, null=False)
    text = models.TextField(blank=False, null=False)
    is_public = models.BooleanField(default=True)
    imagine = models.ImageField(null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class Comment(models.Model):
    created_time = models.DateTimeField(auto_now_add=True)
    text = models.CharField(max_length=256, blank=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)


class Like(models.Model):
    created_time = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)



