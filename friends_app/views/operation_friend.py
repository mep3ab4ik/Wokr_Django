from django.shortcuts import redirect
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from friends_app.models import Friendship
from django.db.models import Q


def operation_friend(request, operation, pk):
    new_friend = get_object_or_404(User, pk=pk)
    # Добавление в друзья(Возможно нужна проверка если ли уже в базе ???)
    if operation == 'add':
        Friendship.objects.get_or_create(sender=request.user, receiver=new_friend)
    # Удаление из друзей
    elif operation == 'remove':
        friend = Friendship.objects.filter((Q(sender=pk) & Q(receiver=request.user.pk)) |
                                           (Q(sender=request.user.pk) & Q(receiver=pk)) & Q(is_accepted=True))[0]
        print(friend)
        # Без удаления не придумал как проще
        if friend:
            friend.sender = pk
            friend.receiver = request.user.pk
            friend.is_accepted = False
            friend.is_sub = True
            friend.save()
    # Подписка на пользователя
    elif operation == 'sub':
        Friendship.get_or_create(sender=request.user.pk, receiver=new_friend, wait_answer=False)
    # Отписка от пользователя, следовательно, удаление из базы
    elif operation == 'unsub':
        friend = Friendship.filer(Q(sender=request.user.pk) & Q(receiver=pk) & Q(is_accepted=False))
        friend.remove()

    return redirect(f'/user/{pk}')
