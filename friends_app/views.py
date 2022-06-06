from django.shortcuts import redirect
from .models import Friend
from django.contrib.auth.models import User


# Create your views here.


def change_friends(request, operations, pk):
    new_friend = User.objects.get(pk=pk)
    if operations == 'add':
        Friend.make_friend(request.user, new_friend)
    elif operations == 'remove':
        Friend.lose_friend(request.user , new_friend)
    return redirect()
