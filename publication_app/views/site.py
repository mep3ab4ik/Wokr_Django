from django.shortcuts import render
from django.views import View
from tag_app.models import Tag
from publication_app.models import Post, Comment, Like, ImagePost
from django.db.models import Count


class Account(View):

    @staticmethod
    def get(request):
        posts = Post.objects.filter(is_public=True).order_by('-created_time', '-id').all()
        comments = Comment.objects.all()
        likes = Like.objects.all()
        image = ImagePost.objects.all()
        tags = Tag.objects.all()
        # count_tag = post
        context = {
            'title': "Hello bit",
            'posts': posts,
            'image': image,
            'comments': comments,
            'likes': likes,
            'tag': tags
        }
        return render(request, 'publication_app/site.html', context)

