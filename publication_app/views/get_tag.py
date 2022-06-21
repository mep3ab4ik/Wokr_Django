from django.shortcuts import render
from django.views import View

from tag_app.models import Tag
from publication_app.models import Post, ImagePost


class GetTag(View):
    """
    View получение тегов и перехожу к постам по тегу
    """
    @staticmethod
    def get(request, tag):
        # Получаем все теги
        our_tag = Tag.objects.filter(tag=tag)

        # Получаем имя тега, когда пользователь перешел по тегу
        for i in our_tag:
            id_tag = i.pk
            name_tag = i.tag

        # Получаем посты по определённому тегу
        posts = Post.objects.filter(tag__id=id_tag)

        tags = Tag.objects.all()

        context = {
            'title': 'Посты по тегам',
            'name_text': f'Публикации по тегу "{name_tag}"',
            'posts': posts,
            'tag': tags,
            'name_tag': name_tag,
        }
        return render(request, 'profile_app/main_page.html', context)


