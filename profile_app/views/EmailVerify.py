from django.contrib.auth import login, get_user_model
from django.core.exceptions import ValidationError
from django.utils.http import urlsafe_base64_decode
from django.views import View
from django.shortcuts import redirect
from django.contrib.auth.tokens import default_token_generator as token_generator

# Можно также использоваться from django.contrib.auth.models import User
# Мы должны использовать get_user_model() чтобы убедиться, что вы получили правильную модель.
# Ибо это используется, когда пишете приложение для многократного использования

User = get_user_model()


class EmailVerify(View):

    def get(self, request, uidb64, token):
        # Вызываем функция получение пользователя
        user = self.get_user(uidb64)

        # Если user есть и токен верен для этого пользователя, то
        if user is not None and token_generator.check_token(user, token):

            # Переводим email_verify в True
            user.profile.email_verify = True

            # Не забываем сохранить изменения
            user.profile.save()
            # Авторизуемся
            login(request, user)
            return redirect('your_account')
        # Иначе редирект, на страницу о некорректной ссылке
        return redirect('invalid_verify')

    @staticmethod
    # Функция получение пользователя
    def get_user(uidb64):
        try:

            # urlsafe_base64_decode() decodes to bytestring
            uid = urlsafe_base64_decode(uidb64).decode()

            # Получаем пользователя по полученному uid
            user = User.objects.get(pk=uid)

        # Если его нет передаем None
        except (TypeError, ValueError, OverflowError,
                User.DoesNotExist, ValidationError):
            user = None
        return user