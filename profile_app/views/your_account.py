from django.shortcuts import render
from django.views import View
from publication_app.models import Post


class YourAccount(View):

    @staticmethod
    def get(request):
        post = Post.objects.filter(user=request.user.pk)
        context = {
            'title': 'Информация о вашем аккаунте',
            'posts': post,
        }
        return render(request, 'profile_app/your_account.html', context)
