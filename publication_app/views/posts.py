from django.shortcuts import render
from django.views import View
from django.db.models import Q

from tag_app.models import Tag
from publication_app.models import Post
from friends_app.models import Friendship


class Posts(View):

    @staticmethod
    def get(request):
        # Запрос на получение всех твоих друзей и кого ты подписан
        friendship = Friendship.objects.filter(Q(sender=request.user.pk) |
                                                (Q(receiver=request.user.pk) & Q(is_accepted=True)))
        print(friendship)
        # Если у тебя друзья или фолловеры:
        if friendship:
            tags = Tag.objects.all()
            # TODO ПОНЯТЬ КАК СДЕЛАТЬ СВОЙ QUERY SET
            post = Post.objects.filter(is_public=True)
            # Переписать запрос
            for user in friendship:
                pass


            # Проверка на наличие постов у "друзей"
            # print(all)
            if post:
                context = {
                    'title': "Посты",
                    'name_text': 'Публикации',
                    'posts': post,
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

