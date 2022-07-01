from rest_framework import routers

from .comment import CommentView

api_routers = routers.DefaultRouter()
api_routers.register('comments', CommentView)
