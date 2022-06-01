from django.contrib import admin
from .models import FriendList, FriendRequest


@admin.register(FriendList)
class FriendListAdmin(admin.ModelAdmin):
    list_filter = ['user']
    list_display = ['user']
    list_display = ['user']
    search_fields = ['user']
    # readonly_fields = ['user']

    class Meta:
        model = FriendList


@admin.register(FriendRequest)
class FriendRequestAdmin(admin.ModelAdmin):
    list_filter = ['sender', 'receiver']
    list_display = ['sender', 'receiver']
    list_display = ['sender', 'receiver']
    search_fields = ['sender__username', 'receiver__username','sender__email', 'receiver__email']

    class Meta:
        model = FriendRequest