from django.contrib.auth.models import User
from tag_app.models import Tag, Hashtag
from media_app.models import Media

from django.db import models
from django.urls import reverse


class Post(models.Model):
    created_time = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=256, unique=False, blank=False, null=False, verbose_name='Название поста')
    text = models.TextField(blank=False, null=False, verbose_name='Текст к посту')
    is_public = models.BooleanField(default=True, null=True, verbose_name='Доступна всем ?')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
    tag = models.ManyToManyField(Tag, blank=True, related_name='tag_post')
    file = models.ForeignKey(Media, on_delete=models.SET_NULL, null=True, blank=True)


    def __str__(self):
        return f'{self.id}.{self.title}'


    def get_absolute_url(self):
        return reverse('read_post', kwargs={'pk': self.pk})


    class Meta:
        # имя в единственном числе
        verbose_name = 'Пост'
        # имя в множественном числе
        verbose_name_plural = 'Посты'
        # заранее установленная сортировка (не требует писать objects.order_by()) и в админки тоже сразу сортирует
        ordering = ['-created_time', '-id']


class ImagePost(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='imageposts')
    image = models.ImageField(upload_to='posts/%Y', null=True, blank=True, verbose_name='Фото')
    uploaded_at = models.DateTimeField(auto_now_add=True)


    def get_absolute_url(self):
        return f'/image{self.id}'

    class Meta:
        verbose_name = 'Фотография  поста'
        verbose_name_plural = 'Фотограции постов'


class HashtagPost(models.Model):
    hashtag = models.ForeignKey(Hashtag, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='hashtag_post')


