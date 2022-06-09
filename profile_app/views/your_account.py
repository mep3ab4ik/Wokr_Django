from django.shortcuts import render
from django.views import View
from publication_app.models import Post
from friends_app.models import Friendship
from django.db.models import Q


class YourAccount(View):

    @staticmethod
    def get(request):
        post = Post.objects.filter(user=request.user.pk)
        friend = Friendship.objects.filter(Q(sender=request.user.pk) | Q(receiver=request.user.pk)).filter(is_accepted=True)
        sub = Friendship.objects.filter(sender=request.user.pk, is_sub=True)
        wait_answer = Friendship.objects.filter(receiver=request.user.pk, wait_answer=True)
        context = {
            'title': 'Информация о вашем аккаунте',
            'posts': post,
            'friends': friend,
            'subs': sub,
            'wait_answers': wait_answer,
        }
        return render(request, 'profile_app/your_account.html', context)
