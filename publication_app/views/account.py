from django.shortcuts import render
from publication_app.models import Post, Comment,Like


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
