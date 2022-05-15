from django.urls import path
from mainpage_app.views import MainPage

urlpatterns = [
    path('', MainPage.as_view(), name='main_page'),
]