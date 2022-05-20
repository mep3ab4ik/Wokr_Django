from django.shortcuts import render
from django.views import View
from profile_app.models import Profile
from publication_app.models import Post, ImagePost


class YourAccount(View):

    @staticmethod
    def get(request):
        profile = Profile.objects.all()
        post = Post.objects.filter(user=request.user.pk)
        image = ImagePost.objects.all()
        context = {
            'title': 'Информация о вашем аккаунте',
            'profile': profile,
            'posts': post,
            'image': image,
        }
        return render(request, 'profile_app/your_account.html', context)
