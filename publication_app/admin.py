from django.contrib import admin
from django.utils.html import mark_safe

# Register your models here.
from .models import *


class HashtagWithPost(admin.StackedInline):
    model = HashtagPost
    list_display = ('id', 'hashtag')
    ordering = ('-id', )

class PostWithImage(admin.StackedInline):
    model = ImagePost
    list_display = ('id', 'image_tag', 'post_id')
    ordering = ('-post_id',)
    readonly_fields = ('image_tag',)

    def image_tag(self, obj):
        if obj.image:
            return mark_safe(
                f'<a href="{obj.image.url}">'
                f'<img src="{obj.image.url}" width ="150" height="150" />'
                f'</a>'
            )

    image_tag.short_description = 'Фото к посту'
    image_tag.allow_tags = True


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    inlines = (
        PostWithImage,
        HashtagWithPost,
    )
    list_display = ('id', 'created_time', 'title')
    ordering = ('-created_time', '-id')
    readonly_fields = ('created_time',)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'created_time', 'text')
    ordering = ('-created_time', '-id')
    readonly_fields = ('created_time',)


@admin.register(Like)
class LikeAdmin(admin.ModelAdmin):
    list_display = ('id', 'user_id', 'post_id')
    ordering = ('-created_time', '-id')
    readonly_fields = ('created_time',)
