from django import forms
from django.contrib.auth.models import User
from publication_app.models import Profile


class UserEditForm(forms.ModelForm):
    """Класс форма редактирование User"""
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']


class ProfileEditForm(forms.ModelForm):
    """Класс форма редактирование Profile"""
    class Meta:
        model = Profile
        fields = ['date_of_birth', 'photo']