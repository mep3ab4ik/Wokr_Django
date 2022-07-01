from rest_framework import routers

from .publications import PostView

api_routers = routers.DefaultRouter()
api_routers.register('posts', PostView)
