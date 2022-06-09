from django.contrib.auth.decorators import login_required
from django.urls import path

from .views.register import Register
from .views.login import UserLogin
from .views.user_logout import user_logout
from .views.user_redaction import UserRedaction
from .views.your_account import YourAccount
from .views.mainpage import MainPage
from .views.profile_user import ProfileUserView



urlpatterns = [
    path('', MainPage.as_view(), name='main_page'),
    path('register/', Register.as_view(), name='register'),
    path('login/', UserLogin.as_view(), name='login'),
    path('logout/', user_logout, name='logout'),
    path('redaction/', login_required(UserRedaction.as_view()), name='redaction'),
    path('your_account/', login_required(YourAccount.as_view()), name='your_account'),
    path('user/<int:pk>', ProfileUserView.as_view(), name='user_account'),
    ]

