from django.urls import path

from .views import UserSearchListView


urlpatterns = [
    path('search/', UserSearchListView.as_view(), name='search_user'),
]
