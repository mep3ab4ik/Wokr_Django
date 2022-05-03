import random

from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView

from .models import Post, Comment, Like
# Create your views here.


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


# class RegisterUser(CreateView):
#     form_class = UserCreationForm
#     template_name = 'register.html'
#     success_url = reverse_lazy('login')
#
#     def get_context_data(self, *, object_list=None, **kwargs):
#         context = super().get_context_data(**kwargs)
#         c_def = self.get_user_context(title="Registration")
#         return dict(list(context.items()) + list(c_def.items()))