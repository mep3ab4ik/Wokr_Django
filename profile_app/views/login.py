from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy

from profile_app.forms.loginform import LoginUserForm


class UserLogin(LoginView):
    """Класс авторизации пользователей."""
    # Подключаем форму
    form_class = LoginUserForm

    # Указываем путь к template для авторизации
    template_name = 'profile_app/login.html'

    # Включаем переадресация для авторизированных пользователей
    redirect_authenticated_user = True

    # Если авторизированны, то куда будет переадресация
    next_page = reverse_lazy('posts')
