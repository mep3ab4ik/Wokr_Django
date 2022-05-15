from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.decorators import login_required
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path

from profile_app.views.register import Register
from profile_app.views.login import UserLogin
from profile_app.views.user_logout import user_logout
from profile_app.views.user_redaction import UserRedaction
from profile_app.views.your_account import YourAccount

urlpatterns = [
    path('register/', Register.as_view(), name='register'),
    path('login/', UserLogin.as_view(), name='login'),
    path('logout/', user_logout, name='logout'),
    path('redaction/', login_required(UserRedaction.as_view()), name='redaction'),
    path('your_account/', login_required(YourAccount.as_view()), name='your_account'),
    ]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += staticfiles_urlpatterns()