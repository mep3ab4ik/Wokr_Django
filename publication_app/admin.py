from django.contrib import admin

# Register your models here.
from .models import Post, Comment, Like


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
