from django.shortcuts import render, redirect
from publication_app.forms.loginform import LoginUserForm
from django.contrib.auth import login
from django.views import View


class UserLogin(View):

    @staticmethod
    def get(request):
        form = LoginUserForm()
        return render(request, 'login.html', {'form': form})

    @staticmethod
    def post(request):
        form = LoginUserForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('account')


