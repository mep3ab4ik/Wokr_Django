from django.shortcuts import render, redirect
from django.views import View
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from friends_app.models import Friendship
from django.db.models import Q


class ProfileUserView(View):

    @staticmethod
    def get(request, pk):
        users = get_object_or_404(User, pk=pk)

        # Проверка, если перешел на свой аккаунт
        if users.pk == request.user.pk:
            return redirect('your_account')

        friend = Friendship.objects.filter(Q(sender=pk) | Q(receiver=pk)).filter(is_accepted=True)
        sub = Friendship.objects.filter(sender=pk, is_sub=True)

        # Один запрос в базу с первым результатом
        is_friendship = Friendship.objects.filter((Q(sender=pk) & Q(receiver=request.user.pk)) |
                                                  (Q(sender=request.user.pk) & Q(receiver=pk)))

        is_friend = None
        is_subscribed = None
        is_follower = None

        # Если ли запись в бд
        if not is_friendship:
            "???"
            pass
        # Проверка на дружбу
        elif is_friendship.filter(is_accepted=True):
            is_friend = True
        # Проверка, что ты подписчик
        elif is_friendship.filter(Q(sender=request.user.pk) & Q(is_sub=True)):
            is_subscribed = True
        # Проверка, что ты фолловер
        elif is_friendship.filter(Q(receiver=request.user.pk) & Q(is_sub=True)):
            is_follower = True
        # else:
        #     is_friend = None
        #     is_subscribed = None
        #     is_follower = None

        context = {
            'title': f'Профиль {users.username}',
            'users': users,
            'friends': friend,
            'subs': sub,
            'is_friend': is_friend,
            'is_subscribed': is_subscribed,
            'is_follow': is_follower,
        }
        return render(request, 'profile_app/profileuser.html', context)

    @staticmethod
    def post(request, operator, pk):
        pass
        # new_request = request.POST.copy()
        # new_request['user'] = request.user.pk
        # new_request['post'] = pk
        # print(new_request)
        # form = AddCommentsForm(data=new_request)
        # if form.is_valid:
        #     form.save()
        #     return redirect(f'/post/{pk}')
