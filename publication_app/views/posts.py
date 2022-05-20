from django.shortcuts import render
from django.views import View
from tag_app.models import Tag
from publication_app.models import Post, Comment, Like, ImagePost



class Account(View):

    @staticmethod
    def get(request):
        posts = Post.objects.filter(is_public=True)
        comments = Comment.objects.all()
        likes = Like.objects.all()
        image = ImagePost.objects.all()
        tags = Tag.objects.all()
        context = {
            'title': "Посты",
            'name_text': 'Публикации',
            'posts': posts,
            'image': image,
            'comments': comments,
            'likes': likes,
            'tag': tags
        }
        return render(request, 'publication_app/posts.html', context)

