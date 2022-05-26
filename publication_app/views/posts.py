from django.shortcuts import render
from django.views import View
from tag_app.models import Tag
from publication_app.models import Post


class Posts(View):

    @staticmethod
    def get(request):
        posts = Post.objects.filter(is_public=True)
        tags = Tag.objects.all()
        context = {
            'title': "Посты",
            'name_text': 'Публикации',
            'posts': posts,
            'tag': tags
        }
        return render(request, 'publication_app/posts.html', context)

