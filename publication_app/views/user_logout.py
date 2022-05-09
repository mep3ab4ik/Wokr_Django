from django.shortcuts import redirect
from django.contrib.auth import logout


def user_logout(request):
    """Функция выхода из аккаунта"""
    logout(request)
    return redirect('login')