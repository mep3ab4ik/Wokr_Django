from django.contrib.auth.decorators import login_required
from django.urls import path

from friends_app.views.operation_friend import operation_friend

urlpatterns = [
    path('connect/<str:operations>/<int:pk>', operation_friend, name='oper_friend')
]