from django.contrib import admin
from .models import Chat


@admin.register(Chat)
class FriendshipAdmin(admin.ModelAdmin):
    list_filter = ['sender', 'recipient', ]
    list_display = ['sender', 'recipient', ]
    search_fields = ['sender', 'recipient', ]


    class Meta:
        model = Chat
