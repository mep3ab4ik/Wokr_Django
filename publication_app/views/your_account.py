from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from publication_app.models import Profile


@login_required()
def your_account(request):
    """Функция отображение своего профиля"""
    profile = Profile.objects.all()
    return render(request, 'Your_account.html', {'profile': profile})