from django.contrib import admin
from .models import Tag
# Register your models here.


@admin.register(Tag)
class Tag(admin.ModelAdmin):
    list_display = ('id', 'tag')
    ordering = ('-id',)

