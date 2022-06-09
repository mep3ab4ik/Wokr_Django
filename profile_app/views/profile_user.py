from django.shortcuts import render
from django.views import View
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from friends_app.models import Friendship
from django.db.models import Q


class ProfileUserView(View):

    @staticmethod
    def get(request, pk):
        users = get_object_or_404(User, pk=pk)
        friend = Friendship.objects.filter(Q(sender=pk) | Q(receiver=pk)).filter(is_accepted=True)
        sub = Friendship.objects.filter(sender=pk, is_sub=True)
        context = {
            'title': f'Профиль {users.username}',
            'users': users,
            'friends': friend,
            'subs': sub,

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