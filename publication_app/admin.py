from django.contrib import admin
from django.utils.html import mark_safe

# Register your models here.
from .models import *


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'date_of_birth', 'photo_tag' )
    ordering = ('-user',)
    readonly_fields = ('photo_tag',)

    def photo_tag(self, obj):
        if obj.photo:
            return mark_safe(f'<img src="{obj.photo.url}" width ="150" height="150" />')

    photo_tag.short_description = 'Image'
    photo_tag.allow_tags = True


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'created_time', 'title', 'imagine_tag')
    ordering = ('-created_time', '-id')
    readonly_fields = ('created_time', 'imagine_tag')


    def imagine_tag(self, obj):
        if obj.imagine:
            return mark_safe(f'<img src="{obj.imagine.url}" width ="150" height="150" />')

    imagine_tag.short_description = 'Image'
    imagine_tag.allow_tags = True



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
