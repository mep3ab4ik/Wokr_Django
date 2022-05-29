from django.db import models
from django.urls import reverse
# Create your models here.


class Tag(models.Model):
    tag = models.CharField(max_length=128, null=False, blank=False, unique=True)



    def __str__(self):
        return f'{self.tag}'

    

    class Meta:
        verbose_name = 'Тэг'
        verbose_name_plural = 'Тэги'


class Hashtag(models.Model):
    hashtag = models.CharField(max_length=64, null=True, blank=True, unique=True)

    def __str__(self):
        return f'{self.id}.{self.hashtag}'


    class Meta:
        verbose_name = 'Хэштег'
        verbose_name_plural = 'Хэштеги'


