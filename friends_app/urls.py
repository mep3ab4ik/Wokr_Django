from django.contrib.auth.decorators import login_required
from django.urls import path, include

from friends_app.views.operation_friend import operation_friend
from .api.views.routrer import api_routers


urlpatterns = [
    path('connect/<str:operation>/<int:pk>', login_required(operation_friend), name='operation_friend'),
    path('api/', include(api_routers.urls)),
]