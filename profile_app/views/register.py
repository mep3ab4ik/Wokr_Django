from django.shortcuts import render, redirect
from profile_app.forms.registerform import RegisterUserForm
from django.contrib.auth import login
from django.contrib import messages
from django.views import View
from django.core.mail import EmailMessage
from django.core.mail import send_mail
from django.core import mail

from profile_app.utils import send_email_for_verify
from tms_kerz.settings import EMAIL_HOST_USER


class Register(View):

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

            # Отправка письма для верификации почты (написано в utils.py)
            send_email_for_verify(request, user)
            return redirect('confirm_email')

        else:
            messages.error(request, 'Ошибка регистрации. Попробуйте снова')
            context = {
                'title': 'Регистрация ',
                'form': form
            }
            return render(request, 'profile_app/register.html', context)

