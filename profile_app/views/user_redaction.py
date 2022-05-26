from django.shortcuts import render, redirect
from profile_app.forms.edituserform import UserEditForm, ProfileEditForm
from django.views import View



class UserRedaction(View):

    @staticmethod
    def get(request):
        user_form = UserEditForm(instance=request.user)
        profile_form = ProfileEditForm(instance=request.user.profile)
        context = {
            'title': 'Редактирование профиля',
            'user_form': user_form,
            'profile_form': profile_form,
        }
        return render(request,
                      'profile_app/redaction_profile.html',
                      context)

    @staticmethod
    def post(request):
        # параметр 'instance' заполняет поля, если в бд есть данные
        user_form = UserEditForm(instance=request.user, data=request.POST)
        profile_form = ProfileEditForm(instance=request.user.profile, data=request.POST, files=request.FILES)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return redirect('your_account')
