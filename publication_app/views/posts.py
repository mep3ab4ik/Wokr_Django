from django.shortcuts import render
from django.views import View
from django.db.models import Q
from django.core.paginator import Paginator

from tag_app.models import Tag
from publication_app.models import Post
from friends_app.models import Friendship


class Posts(View):

    @staticmethod
    def get(request):
        # Запрос на получение всех твоих друзей и кого ты подписан
        friendship = Friendship.objects.filter(Q(sender=request.user.pk) |
                                               (Q(receiver=request.user.pk) & Q(is_accepted=True)))

        # Объявляем пустой список для id друзей\фоловеров
        users = [request.user.pk]

        for friend in friendship:

            if friend.sender.pk not in users:
                users.append(friend.sender.pk)

            if friend.receiver.pk not in users:
                users.append(friend.receiver.pk)

        # Если у тебя друзья или фолловеры:
        if users:
            posts = Post.objects.filter(is_public=True).filter(user__in=users)

            # Проверка на наличие постов у "друзей"
            if posts:

                tags = Tag.objects.all()

                # Пагинация Queryset по 3 объекта на страницу
                paginator = Paginator(posts, 3)
                # Получаем номер страницы
                page_number = request.GET.get('page')
                # Получаем объект
                page_obj = paginator.get_page(page_number)

                context = {
                    'title': "Посты",
                    'name_text': 'Публикации друзей и фолловеров',
                    'posts': page_obj,
                    'tag': tags,
                    'information': None,
                }

            # Если посты отсутствуют
            else:
                context = {
                    'title': "Посты",
                    'information': 'Вы еще никого не добавили в друзья/фолловеры и не добавили пост. '
                                   'Найдите пользователей или добавьте посты, которые вам интересны'
                }

        return render(request, 'publication_app/posts.html', context)
