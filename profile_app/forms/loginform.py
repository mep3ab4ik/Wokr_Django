from django import forms
from django.contrib.auth import authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.core.exceptions import ValidationError

from profile_app.utils import send_email_for_verify


class LoginUserForm(AuthenticationForm):
    """
    Класс формы авторизации пользователя
    """
    # Переопределение сообщение об ошибки из формы AuthenticationForm
    error_messages = {
        "invalid_login": (
            "Неверные логин или пароль. Попробуйте снова.\n"
            "Обратите внимание, что оба поля чувствительные к регистру."
        ),
    }

    # Переопределение функции из формы AuthenticationForm
    def clean(self):
        # Получаем username и password
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')

        # Проверка, что пользователь ввел пароль и логин
        if username is not None and password:
            # Пытаемся авторизовать пользователя по введённым данным. Возвращает None, если данные неверные или не сущ.
            self.user_cache = authenticate(
                self.request,
                username=username,
                password=password,
            )

            # Проверка, что пользователь не смог авторизоваться. Тогда выдаем ошибку.
            if self.user_cache is None:
                raise self.get_invalid_login_error()
            else:
                self.confirm_login_allowed(self.user_cache)

            # Если пользователь смог авторизоваться, то проверяем поле email_verify
            if not self.user_cache.profile.email_verify:

                # Если почта не подтверждённая, то высылаем снова письма данному пользователь
                send_email_for_verify(self.request, self.user_cache)

                # Выдаем пользователю ошибку
                raise ValidationError(
                    'Почта не подтверждена, проверьте Email для подтверждения',
                    code='invalid',
                )

        return self.cleaned_data

