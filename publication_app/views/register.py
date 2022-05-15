from django.shortcuts import render, redirect
from publication_app.forms.registerform import RegisterUserForm
from publication_app.models import Profile
from django.contrib.auth import login
from django.contrib import messages
from django.views import View


class Register(View):

    @staticmethod
    def get(request):
        form = RegisterUserForm()
        context = {
            'title': 'Регистрация ',
            'form': form
        }
        return render(request, 'register.html', context)

    @staticmethod
    def post(request):
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('account')
        else:
            messages.error(request, 'Ошибка регистрации. Попробуйте снова')

