from django.views import View
from django.shortcuts import render
from tag_app.models import Tag
from publication_app.models import Post, ImagePost


# Создать html для кноки открыть пост нормальный ( На будущее )
class ReadPostView(View):

    @staticmethod
    def get(request, pk):
        posts = Post.objects.filter(pk=pk)
        image = ImagePost.objects.filter(post=pk)
        tags = Tag.objects.all()
        context = {
            'title': 'Пост',
            'name_text': 'Публикации',
            'posts': posts,
            'image': image,
            'tag': tags
        }
        return render(request, 'publication_app/posts.html', context)