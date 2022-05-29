from django.urls import path, include
from .api.views.router import api_routers

urlpatterns = [
    path('api/', include(api_routers.urls)),
]
