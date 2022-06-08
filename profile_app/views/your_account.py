from django.shortcuts import render
from django.views import View
from publication_app.models import Post
from friends_app.models import Friendship


class YourAccount(View):

    @staticmethod
    def get(request):
        post = Post.objects.filter(user=request.user.pk)
        friend = Friendship.objects.filter(sender=request.user.pk, is_accepted=True)
        sub = Friendship.objects.filter(sender=request.user.pk, is_sub=True)

        context = {
            'title': 'Информация о вашем аккаунте',
            'posts': post,
            'friends': friend,
            'subs': sub,
        }
        return render(request, 'profile_app/your_account.html', context)
