from django.contrib.auth.decorators import login_required
from django.urls import path

from chat_app.views.ChatMessageView import ChatMessageView

urlpatterns = [
    path('message/<int:pk>', login_required(ChatMessageView.as_view()), name='chat'),

]
