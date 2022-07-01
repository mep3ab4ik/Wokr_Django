from rest_framework import routers

from .like import LikeView

api_routers = routers.DefaultRouter()
api_routers.register('likes', LikeView)
