from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path

from publication_app.views.account import account
from publication_app.views.login import user_login
from publication_app.views.main_page import main_page
from publication_app.views.register import register
from publication_app.views.user_logout import user_logout
from publication_app.views.user_redaction import user_redaction
from publication_app.views.your_account import your_account
from publication_app.views.add_post import add_post
from publication_app.views.edit_post import edit_post
from publication_app.views.delete_post import delete_post

urlpatterns = [
    path('', main_page, name='main_page'),
    path('account/', account, name='account'),
    path('register/', register, name='register'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
    path('redaction/', user_redaction, name='redaction'),
    path('your_account/', your_account, name='your_account'),
    path('add_post/', add_post, name='add_post'),
    path('edit_post/<int:pk>', edit_post, name ='edit_post'),
    path('delete_post/<int:pk>', delete_post, name='delete_post')
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += staticfiles_urlpatterns()