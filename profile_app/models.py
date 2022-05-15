from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    date_of_birth = models.DateTimeField(blank=True, null=True, verbose_name='Дата рождения')
    photo = models.ImageField(upload_to='users/%Y', blank=True, verbose_name='Аватар')

    def __str__(self):
        return f'Profile for user {self.user.username}'