from django.shortcuts import render, redirect
from publication_app.forms.registerform import RegisterUserForm
from publication_app.models import Profile
from django.contrib.auth import login
from django.contrib import messages


def register(request):
    """Функция регистрации пользователя"""
    if request.method == 'POST':
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            # Создает связять между Profile и User по ключу
            Profile.objects.create(user=user)
            login(request, user)
            return redirect('account')
        else:
            messages.error(request, 'Ошибка регистрации')
    else:
        form = RegisterUserForm()
    return render(request, 'register.html', {'form': form})