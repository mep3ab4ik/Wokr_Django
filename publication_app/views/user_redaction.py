from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from publication_app.forms.EditUserForm import UserEditForm, ProfileEditForm


@login_required()
def user_redaction(request):
    """Функция редактирования пользователя"""
    if request.method == 'POST':
        # параметр 'instance' заполняет поля, если в бд есть данные (ХОТЯ В ДУШЕ НЕ ЕБУ))
        user_form = UserEditForm(instance=request.user, data=request.POST)
        profile_form = ProfileEditForm(instance=request.user.profile, data=request.POST, files=request.FILES)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return redirect('account')
    else:
        user_form = UserEditForm(instance=request.user)
        profile_form = ProfileEditForm(instance=request.user.profile)
        return render(request,
                      'redaction_profile.html',
                      {'user_form': user_form,
                       'profile_form': profile_form})