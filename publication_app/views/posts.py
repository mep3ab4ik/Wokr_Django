from django.shortcuts import render
from django.views import View
from django.db.models import Q

from tag_app.models import Tag
from publication_app.models import Post
from friends_app.models import Friendship


class Posts(View):

    @staticmethod
    def get(request):
        # Запрос на получение всех друзей и кого ты подписан(Тут выдает на кого ты подписан)
        friendship = Friendship.objects.filter(Q(sender=request.user.pk) |
                                                (Q(receiver=request.user.pk) & Q(is_accepted=True)))
        print(friendship)
        # Если у тебя друзья или фолловеры:
        if friendship:
            for user in friendship:
                posts = Post.objects.filter(is_public=True).filter(Q(user=user.sender) | Q(user=user.receiver))
                tags = Tag.objects.all()

            # Проверка на наличие постов у "друзей"
                if posts:
                    context = {
                        'title': "Посты",
                        'name_text': 'Публикации',
                        'posts': posts,
                        'tag': tags
                    }
                # Если посты отсутствуют
                else:
                    context = {
                        'title': "Посты",
                        'information': 'У вашей друзей/фолловеров нет постов. '
                                       'Найдите новых пользователей, которые вам интересны'
                    }
        else:
            context = {
                'title': "Посты",
                'information': 'Вы еще никого не добавили в друзья/фолловеры. Найдите пользователей, которые вам интересны'
            }
        # # posts = Post.objects.filter(is_public=True)
        # # tags = Tag.objects.all()
        # context = {
        #     'title': "Посты",
        #     'name_text': 'Публикации',
        #     'posts': posts,
        #     'tag': tags
        # }
        return render(request, 'publication_app/posts.html', context)

