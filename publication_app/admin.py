from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as UserAdminBase
from django.contrib.auth.models import User
from django.utils.html import mark_safe

# Register your models here.
from .models import *

admin.site.unregister(User)


# @admin.register(Profile)
# class ProfileAdmin(admin.ModelAdmin):
#     list_display = ('user', 'date_of_birth', 'photo_tag' )
#     ordering = ('-user',)
#     readonly_fields = ('photo_tag',)
#
#     def photo_tag(self, obj):
#         if obj.photo:
#             return mark_safe(f'<img src="{obj.photo.url}" width ="150" height="150" />')
#
#     photo_tag.short_description = 'Image'
#     photo_tag.allow_tags = True

class ProfileInline(admin.StackedInline):
    model = Profile

    list_display = ('user', 'date_of_birth', 'photo_tag')
    ordering = ('-user',)
    readonly_fields = ('photo_tag',)

    def photo_tag(self, obj):
        if obj.photo:
            return mark_safe(f'<img src="{obj.photo.url}" width ="150" height="150" />')

    photo_tag.short_description = 'Аватар'
    photo_tag.allow_tags = True


@admin.register(User)
class UserAdmin(UserAdminBase):
    inlines = (
        ProfileInline,
    )


@admin.register(ImagePost)
class PostWithImage(admin.ModelAdmin):

    list_display = ('id', 'image_tag', 'post_id')
    ordering = ('-post_id',)
    readonly_fields = ('image_tag',)

    def image_tag(self, obj):
        if obj.image:
            return mark_safe(f'<img src="{obj.image.url}" width ="150" height="150" />')

    image_tag.short_description = 'Фото к посту'
    image_tag.allow_tags = True


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
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
