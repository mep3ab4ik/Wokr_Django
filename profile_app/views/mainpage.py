from django.shortcuts import render
from django.views import View
from django.core.paginator import Paginator

from publication_app.models import Post
from tag_app.models import Tag


class MainPage(View):
    """Класс главной страницы"""
    @staticmethod
    def get(request):
        posts = Post.objects.filter(is_public=True)
        tags = Tag.objects.all()
        # Пагинация Queryset по 3 объекта на страницу
        paginator = Paginator(posts, 3)
        # Получаем номер страницы
        page_number = request.GET.get('page')
        # Получаем объект
        page_obj = paginator.get_page(page_number)

        # Для проверки
        # posts = ({'title': random.randint(100,1_000_000), 'text': 'dgrrg5gerbht5w4ytget645464'} for _ in range(100))

        context = {
            'title': "Kerz Django",
            'posts': page_obj,
            'tag': tags,
        }
        return render(request, 'profile_app/main_page.html', context)
