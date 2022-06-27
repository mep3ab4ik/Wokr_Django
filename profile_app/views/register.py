from django.shortcuts import render, redirect
from django.contrib.sites.shortcuts import get_current_site
from django.contrib import messages
from django.views import View
import logging

from profile_app.tasks import send_email_for_verify
from profile_app.forms.registerform import RegisterUserForm

logger = logging.getLogger('main')




class Register(View):
    """Класс регистрации пользователя"""
    @staticmethod
    def get(request):

        if request.user.is_authenticated:
            return redirect('posts')

        form = RegisterUserForm()

        context = {
            'title': 'Регистрация ',
            'form': form
        }
        return render(request, 'profile_app/register.html', context)

    @staticmethod
    def post(request):
        form = RegisterUserForm(request.POST)

        if form.is_valid():
            user = form.save()

            # Получаем домен перед передачей в celerу, так как он может принимать только конкретные значение
            current_site = get_current_site(request)
            # Отправка письма для верификации почты (написано в tasks.py)
            logging.info(send_email_for_verify(current_site.domain, user.pk))
            return redirect('confirm_email')

        else:
            messages.error(request, 'Ошибка регистрации. Попробуйте снова')

            context = {
                'title': 'Регистрация ',
                'form': form
            }
            return render(request, 'profile_app/register.html', context)

