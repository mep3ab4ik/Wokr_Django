from django.conf import settings
from django.conf.urls.static import static

from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path
from mainpage_app.views import MainPage

urlpatterns = [
    path('', MainPage.as_view(), name='main_page'),
]