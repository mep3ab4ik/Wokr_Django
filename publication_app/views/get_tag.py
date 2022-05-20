from django.shortcuts import render
from django.views import View

from tag_app.models import Tag, Hashtag
from publication_app.models import Post, ImagePost


class GetTag(View):

    @staticmethod
    def get(request, tag):
        our_tag = Tag.objects.filter(tag=tag)
        for i in our_tag:
            id_tag = i.pk
            name_tag = i.tag
        posts = Post.objects.filter(tag__id=id_tag)
        tags = Tag.objects.all()
        image = ImagePost.objects.all()
        context = {
            'title': 'Посты по тегам',
            'name_text': f'Публикации по тегу "{name_tag}"',
            'posts': posts,
            'image': image,
            'tag': tags,
            'name_tag': name_tag,
        }
        return render(request, 'publication_app/posts.html', context)


