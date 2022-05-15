from django.contrib.auth.models import User
from django.db import models


# Create your models here.


class Post(models.Model):
    created_time = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=256, unique=False, blank=False, null=False, verbose_name='Название поста')
    text = models.TextField(blank=False, null=False, verbose_name='Текст к посту')
    is_public = models.BooleanField(default=True, null=True, verbose_name='Доступна всем ?')
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return '/account'


class ImagePost(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='imageposts')
    image = models.ImageField(upload_to='posts/%Y', null=True, blank=True, verbose_name='Фото')
    uploaded_at = models.DateTimeField(auto_now_add=True)


    @staticmethod
    def get_absolute_url():
        return '/account'


class Comment(models.Model):
    created_time = models.DateTimeField(auto_now_add=True)
    text = models.CharField(max_length=256, blank=False, verbose_name='Комментарий')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)


class Like(models.Model):
    created_time = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
