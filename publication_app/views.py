import random

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login, logout

from django.urls import reverse_lazy

from publication_app.forms.registerform import RegisterUserForm
from publication_app.forms.loginform import LoginUserForm
from publication_app.forms.EditUserForm import UserEditForm, ProfileEditForm
from publication_app.forms.add_post import AddPostForm

from .models import *
# Create your views here.


def main_page(request):
    return render(request, 'main_page.html')


def account(request):
    posts = Post.objects.filter(is_public=True).order_by('-created_time', '-id').all()
    comments = Comment.objects.all()
    likes = Like.objects.all()
    # posts = ({'title': random.randint(100,1_000_000), 'text': 'dgrrg5gerbht5w4ytgethngsvrhn2#$%#645464'} for _ in range(100))

    context = {
        'title': "Hello bit",
        'posts': posts,
        'comments': comments,
        'likes': likes,
    }
    return render(request, 'account.html', context)


def register(request):
    if request.method == 'POST':
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            profile = Profile.objects.create(user=user)
            login(request, user)
            return redirect('account')
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
            return redirect('account')
    else:
        form = LoginUserForm()

    return render(request, 'login.html', {'form': form})


def user_logout(request):
    logout(request)
    return redirect('login')


@login_required()
def user_redaction(request):
    if request.method == 'POST':
        user_form = UserEditForm(instance=request.user, data=request.POST)
        profile_form = ProfileEditForm(instance=request.user.profile, data = request.POST, files = request.FILES)
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


@login_required()
def your_account(request):
    profile = Profile.objects.all()
    return render(request, 'Your_account.html', {'profile': profile})


@login_required()
def add_post(request):
    if request.method == 'POST':
        form = AddPostForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            new_request = form.cleaned_data
            new_request['user_id'] = request.user.pk
            Post.objects.create(**new_request)
            return redirect('account')
    else:
        form = AddPostForm()
    return render(request, 'add_post.html', {'form': form})

