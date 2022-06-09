from rest_framework import routers

from .friend import MediaViewSet

api_routers = routers.DefaultRouter()
api_routers.register('media', MediaViewSet)