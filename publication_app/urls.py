from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path
from django.contrib.auth.decorators import login_required

from publication_app.views.account import Account
from publication_app.views.login import UserLogin
from publication_app.views.main_page import main_page
from publication_app.views.register import Register
from publication_app.views.user_logout import user_logout
from publication_app.views.user_redaction import UserRedaction
from publication_app.views.your_account import YourAccount
from publication_app.views.add_post import AddPost
from publication_app.views.edit_post import EditImagePost
from publication_app.views.delete_post import delete_post

urlpatterns = [
    path('', main_page, name='main_page'),
    path('account/', Account.as_view(), name='account'),
    path('register/', Register.as_view(), name='register'),
    path('login/', UserLogin.as_view(), name='login'),
    path('logout/', user_logout, name='logout'),
    path('redaction/', login_required(UserRedaction.as_view()), name='redaction'),
    path('your_account/', login_required(YourAccount.as_view()), name='your_account'),
    path('add_post/', login_required(AddPost.as_view()), name='add_post'),
    path('edit_post/<int:pk>', login_required(EditImagePost.as_view()), name='edit_post'),
    path('delete_post/<int:pk>', delete_post, name='delete_post')
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += staticfiles_urlpatterns()