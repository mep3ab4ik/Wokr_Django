from django.contrib.auth.decorators import login_required
from django.urls import path, include

from friends_app.views.operation_friend import operation_friend
from .api.views.routrer import api_routers


urlpatterns = [
    path('connect/<str:operations>/<int:pk>', operation_friend, name='oper_friend'),
    path('api/', include(api_routers.urls)),
]