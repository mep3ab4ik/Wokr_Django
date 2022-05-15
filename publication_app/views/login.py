from django.shortcuts import render, redirect
from publication_app.forms.loginform import LoginUserForm
from django.contrib.auth import login
from django.views import View


class UserLogin(View):

    @staticmethod
    def get(request):
        form = LoginUserForm()
        context = {
            'title': 'Авторизация',
            'form': form
        }
        return render(request, 'login.html', context)

    @staticmethod
    def post(request):
        form = LoginUserForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('account')


