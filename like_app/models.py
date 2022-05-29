from django.db import models
from django.contrib.auth.models import User
from publication_app.models import Post
from comment_app.models import Comment


class Like(models.Model):
    created_time = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_like')
    post = models.ForeignKey(Post, blank=True, null=True, on_delete=models.CASCADE, related_name="post_like")
    comment = models.ForeignKey(Comment, blank=True,null=True, on_delete=models.CASCADE,  related_name='com_like')
