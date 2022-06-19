from rest_framework import routers

from .chat import ChatView

api_routers = routers.DefaultRouter()
api_routers.register('messages', ChatView)
