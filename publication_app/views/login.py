from django.shortcuts import render, redirect
from publication_app.forms.loginform import LoginUserForm
from django.contrib.auth import login


def user_login(request):
    if request.method == 'POST':
        form = LoginUserForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('account')
    else:
        form = LoginUserForm()

    return render(request, 'login.html', {'form': form})