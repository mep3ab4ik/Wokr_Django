from rest_framework import routers

from .media import MediaViewSet

api_routers = routers.DefaultRouter()
api_routers.register('media', MediaViewSet)