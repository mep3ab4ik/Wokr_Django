from django.contrib import admin
from .models import FriendList


@admin.register(FriendList)
class FriendListAdmin(admin.ModelAdmin):
    list_filter = ['user']
    list_display = ['user']
    search_fields = ['user']
    # readonly_fields = ['user']

    class Meta:
        model = FriendList


