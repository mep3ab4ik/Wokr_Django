from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from publication_app.models import Profile, Post


@login_required()
def your_account(request):
    """Функция отображение своего профиля"""
    profile = Profile.objects.all()
    post = Post.objects.order_by('-created_time', '-id').all()

    context = {
        'title': 'Информация о вашем аккаунте',
        'profile': profile,
        'posts': post
    }
    return render(request, 'Your_account.html', context)