from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.views import View
from publication_app.models import Profile, Post, ImagePost


class YourAccount(View):

    @staticmethod
    def get(request):
        profile = Profile.objects.all()
        post = Post.objects.order_by('-created_time', '-id').all()
        image = ImagePost.objects.all()
        context = {
            'title': 'Информация о вашем аккаунте',
            'profile': profile,
            'posts': post,
            'image': image,
        }
        return render(request, 'Your_account.html', context)
