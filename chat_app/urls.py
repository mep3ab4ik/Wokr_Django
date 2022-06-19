from django.contrib.auth.decorators import login_required
from django.urls import path, include
from .api.views.router import api_routers
from .views.ChatMessageView import ChatMessageView

urlpatterns = [
    path('api/', include(api_routers.urls)),
    path('message/<int:pk>', login_required(ChatMessageView.as_view()), name='chat'),
]
