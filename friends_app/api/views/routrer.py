from rest_framework import routers

from .friend import FriendshipViewSet

api_routers = routers.DefaultRouter()
api_routers.register('friendship', FriendshipViewSet)