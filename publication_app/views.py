import random

from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login, logout
from django.urls import reverse_lazy

from publication_app.forms.registerform import RegisterUserForm
from publication_app.forms.loginform import LoginUserForm

from .models import Post, Comment, Like
# Create your views here.


def main_page(request):
    return render(request, 'main_page.html')



def profile(request):
    posts = Post.objects.filter(is_public=True).order_by('-created_time', '-id').all()
    comments = Comment.objects.all()
    likes = Like.objects.all()
    # posts = ({'title': random.randint(100,1_000_000), 'text': 'dgrrg5gerbht5w4ytgethngsvrhn2#$%#645464'} for _ in range(100))

    context = {'title': "Hello bit",
               'posts': posts,
               'comments': comments,
               'likes': likes}
    return render(request, 'Profile.html', context)


def register(request):
    if request.method == 'POST':
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('profile')
        else:
            messages.error(request, 'Ошибка регистрации')
    else:
        form = RegisterUserForm()
    return render(request, 'register.html', {'form': form})


def user_login(request):
    if request.method == 'POST':
        form = LoginUserForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('profile')
    else:
        form = LoginUserForm()

    return render(request, 'login.html', {'form': form})


def user_logout(request):
    logout(request)
    return redirect('login')

