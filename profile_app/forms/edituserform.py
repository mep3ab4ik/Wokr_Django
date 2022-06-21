from django import forms
from django.contrib.auth.models import User
from profile_app.models import Profile


class UserEditForm(forms.ModelForm):
    """Класс форма редактирование User"""
    first_name = forms.CharField(
        label='Ваше Имя'
    )
    last_name = forms.CharField(
        label='Ваша Фамилия'
    )

    class Meta:
        model = User
        fields = ['first_name', 'last_name']


class ProfileEditForm(forms.ModelForm):
    """Класс форма редактирование Profile"""
    date_of_birth = forms.DateField(
        label='Дата рождения',
        help_text="Формат ввода :'г-м-д'. Пример: 2020-01-31",
    )

    class Meta:
        model = Profile
        fields = ['date_of_birth', 'photo']
