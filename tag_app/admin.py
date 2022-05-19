from django.contrib import admin
from .models import Tag, Hashtag
# Register your models here.


@admin.register(Tag)
class Tag(admin.ModelAdmin):
    list_display = ('id', 'tag')
    ordering = ('-id',)


@admin.register(Hashtag)
class Hashtag(admin.ModelAdmin):
    list_display = ('id', 'hashtag')
    ordering = ('-id',)
