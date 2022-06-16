from django.db import models
from django.contrib.auth.models import User


# Обратите внимание, что в документах рекомендуется использовать settings.AUTH_USER_MODEL для внешних ключей.


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    date_of_birth = models.DateTimeField(blank=True, null=True, verbose_name='Дата рождения')
    photo = models.ImageField(upload_to='users/%Y', blank=True, verbose_name='Аватар')
    email_verify = models.BooleanField(default=False)

    def __str__(self):
        return f'Profile for user {self.user.username}'

    class Meta:
        verbose_name = 'Профиль'
        verbose_name_plural = 'Профили'