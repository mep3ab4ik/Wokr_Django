import random

from django.shortcuts import render

from .models import Post
# Create your views here.


def main_page(request):
    posts = Post.objects.filter(is_public=True).order_by('-created_time', '-id').all()
    # posts = ({'title': random.randint(100,1_000_000), 'text': 'dgrrg5gerbht5w4ytgethngsvrhn2#$%#645464'} for _ in range(100))

    context = {'title': "Hello bit",
               'posts': posts}
    return render(request, 'main_page.html', context)