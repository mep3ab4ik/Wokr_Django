from django.shortcuts import render
from django.views import View
from publication_app.models import Post, Comment, Like, ImagePost
from tag_app.models import Tag


class MainPage(View):

    @staticmethod
    def get(request):
        posts = Post.objects.filter(is_public=True)
        comments = Comment.objects.all()
        likes = Like.objects.all()
        image = ImagePost.objects.all()
        tags = Tag.objects.all()
        # Для проверки
        # posts = ({'title': random.randint(100,1_000_000), 'text': 'dgrrg5gerbht5w4ytgethngsvrhn2#$%#645464'} for _ in range(100))
        context = {
            'title': "Kerz Django",
            'posts': posts,
            'image': image,
            'comments': comments,
            'likes': likes,
            'tag': tags,
        }
        return render(request, 'profile_app/main_page.html', context)
