from django.shortcuts import render
from publication_app.models import Post, Comment,Like, ImagePost


def account(request):
    """Функция для генерации постов, комментов и лайков на странице"""

    posts = Post.objects.filter(is_public=True).order_by('-created_time', '-id').all()
    comments = Comment.objects.all()
    likes = Like.objects.all()
    image = ImagePost.objects.all()
    #Для проверки
    # posts = ({'title': random.randint(100,1_000_000), 'text': 'dgrrg5gerbht5w4ytgethngsvrhn2#$%#645464'} for _ in range(100))

    context = {
        'title': "Hello bit",
        'posts': posts,
        'image': image,
        'comments': comments,
        'likes': likes,
    }
    return render(request, 'account.html', context)
