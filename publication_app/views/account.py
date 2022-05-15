from django.shortcuts import render
from django.views import View
from publication_app.models import Post, Comment,Like, ImagePost


class Account(View):

    @staticmethod
    def get(request):
        posts = Post.objects.filter(is_public=True).order_by('-created_time', '-id').all()
        comments = Comment.objects.all()
        likes = Like.objects.all()
        image = ImagePost.objects.all()
        context = {
            'title': "Hello bit",
            'posts': posts,
            'image': image,
            'comments': comments,
            'likes': likes,
        }
        return render(request, 'site.html', context)

