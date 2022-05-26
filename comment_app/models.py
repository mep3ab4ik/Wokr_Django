from django.db import models
from django.contrib.auth.models import User
from publication_app.models import Post


class Comment(models.Model):
    created_time = models.DateTimeField(auto_now_add=True)
    text = models.CharField(max_length=256, blank=False, verbose_name='Комментарий')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='post_com')

    def __str__(self):
        return f'{self.text}'