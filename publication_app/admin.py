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
    list_display = ('id', 'created_time', 'title', 'is_public',)
    ordering = ('-created_time', '-id')
    readonly_fields = ('created_time',)
    # изменять не заходя в пост
    list_editable = ('is_public', )
    # фильтровать по чем
    list_filter = ('is_public',)




