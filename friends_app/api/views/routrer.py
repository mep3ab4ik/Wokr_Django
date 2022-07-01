from rest_framework import routers

from .friend import FriendsViewSet, SubscribeViewSet, UpdateFriendsViewSet
from .subscribe import SubscribeViewSet

api_routers = routers.DefaultRouter()
api_routers.register('friends', FriendsViewSet)
api_routers.register('friends', UpdateFriendsViewSet)
api_routers.register('subscribers', SubscribeViewSet)