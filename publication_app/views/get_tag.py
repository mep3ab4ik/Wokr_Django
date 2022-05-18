from django.shortcuts import render
from tag_app.models import Tag
from publication_app.models import Post, ImagePost


def get_tag(request, tag):
    our_tag = Tag.objects.filter(tag=tag)
    for i in our_tag:
        id_tag = i.pk
        name_tag = i.tag
    posts = Post.objects.filter(tag__id=id_tag)
    tags = Tag.objects.all()
    image = ImagePost.objects.all()
    context = {
        'title': 'Посты по тегам',
        'posts': posts,
        'image': image,
        'tag': tags,
        'name_tag': name_tag,
    }
    return render(request, 'publication_app/tag.html', context)