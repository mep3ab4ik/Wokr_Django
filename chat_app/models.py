from django.db import models
from django.contrib.auth.models import User


class Chat(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='chat_sender')
    recipient = models.ForeignKey(User, on_delete=models.CASCADE, related_name='char_recipient')
    text = models.CharField(max_length=256)
    time = models.DateTimeField(auto_now_add=True)
