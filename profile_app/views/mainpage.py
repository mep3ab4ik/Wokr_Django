from django.shortcuts import render
from django.views import View
from publication_app.models import Post
from tag_app.models import Tag


class MainPage(View):

    @staticmethod
    def get(request):
        posts = Post.objects.filter(is_public=True)
        tags = Tag.objects.all()
        # Для проверки
        # posts = ({'title': random.randint(100,1_000_000), 'text': 'dgrrg5gerbht5w4ytgethngsvrhn2#$%#645464'} for _ in range(100))
        context = {
            'title': "Kerz Django",
            'posts': posts,
            'tag': tags,
        }
        return render(request, 'profile_app/main_page.html', context)
