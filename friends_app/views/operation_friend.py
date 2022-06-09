from django.shortcuts import redirect
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from friends_app.models import Friendship
from django.db.models import Q




def operation_friend(request, operations, pk):
    new_friend = get_object_or_404(User, pk=pk)

    if operations == 'add':
        Friendship.objects.get_or_create(Q(sender=request.user.pk) & Q(receiver=new_friend), )

    elif operations == 'remove':
        friend = Friendship.objects.filter(Q(sender=request.user.pk) & Q(receiver=new_friend) & Q(is_accepted=True))
        if friend:
            friend.delete()

    return redirect(f'/user/{pk}')