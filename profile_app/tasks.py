from django.contrib.sites.shortcuts import get_current_site
from django.core import mail
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode
from django.contrib.auth.tokens import default_token_generator as token_generator

from celery import shared_task

from tms_kerz.settings import EMAIL_HOST_USER


@shared_task
def send_email_for_verify(request, user):
    # С помощью get_current_site получаем домен
    current_site = get_current_site(request)

    # Формирует контекст для сообщения
    # Для создания uid и токена используется user

    context = {
        'user': user,  # Пользователь
        'domain': current_site.domain,  # Домен
        'uid': urlsafe_base64_encode(force_bytes(user.pk)),  # Генерируем uid
        'token': token_generator.make_token(user),  # Генерируем токен
    }

    # Формируем сообщение
    # render_to_string - передает в шаблон контекст, рендерит его и возвращает строкой
    message = render_to_string(
        template_name='profile_app/verify_email.html',
        context=context,
    )



    # Открывает \ закрывает соединение для отправки писем. Можно указать open и close
    with mail.get_connection() as connection:
        email = EmailMessage(
            subject='Veryfi email check',  # Заголовок
            body=message,  # Тело сообщение
            from_email=EMAIL_HOST_USER,  # Кто отправляет
            to=[user.email],  # Кому отправляем
            connection=connection,  # Экземпляр бэкенда электронной почты.
            # Используйте этот параметр, если вы хотите использовать одно и то же соединение для нескольких сообщений.
            # Если параметр опущен, то при вызове send() создается новое соединение.
        )

        # Отправка сообщение
        email.send(fail_silently=False)

