from django.core.paginator import Paginator
from django.shortcuts import render
from django.views import View
from django.db.models import Q


from publication_app.models import Post
from friends_app.models import Friendship


class YourAccount(View):
    """Класс информации о 'своем' аккаунте"""
    @staticmethod
    def get(request):
        # Получаем посты пользователя
        posts = Post.objects.filter(user=request.user.pk)

        # Пагинация Queryset по 3 объекта на страницу
        paginator = Paginator(posts, 3)
        # Получаем номер страницы
        page_number = request.GET.get('page')
        # Получаем объект
        page_obj = paginator.get_page(page_number)

        # Получаем всех друзей
        friend = Friendship.objects.filter(Q(sender=request.user.pk) | Q(receiver=request.user.pk)).\
            filter(is_accepted=True)

        # Получаем всех подписчиков
        sub = Friendship.objects.filter(sender=request.user.pk, is_sub=True)

        # Получаем пользователей, которые нас добавили и ждут решение
        wait_answer = Friendship.objects.filter(receiver=request.user.pk, wait_answer=True)

        context = {
            'title': 'Информация о вашем аккаунте',
            'posts': page_obj,
            'friends': friend,
            'subs': sub,
            'wait_answers': wait_answer,
        }

        return render(request, 'profile_app/your_account.html', context)
