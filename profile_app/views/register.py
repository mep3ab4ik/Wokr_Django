from django.shortcuts import render, redirect
from profile_app.forms.registerform import RegisterUserForm
from django.contrib.auth import login
from django.contrib import messages
from django.views import View


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
            login(request, user)
            return redirect('posts')
        else:
            messages.error(request, 'Ошибка регистрации. Попробуйте снова')
            context = {
                'title': 'Регистрация ',
                'form': form
            }
            return render(request, 'profile_app/register.html', context)

