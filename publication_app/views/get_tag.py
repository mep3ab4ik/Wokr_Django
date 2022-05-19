from django.shortcuts import render
from tag_app.models import Tag, Hashtag
from publication_app.models import Post, ImagePost


def get_tag(request, tag):
    our_tag = Tag.objects.filter(tag=tag)
    for i in our_tag:
        id_tag = i.pk
        name_tag = i.tag
    posts = Post.objects.filter(tag__id=id_tag).order_by('-created_time', '-id')
    tags = Tag.objects.all()
    image = ImagePost.objects.all()

    hah = Hashtag.objects.filter(post=41)
    print(hah)
    pos45 = Post.objects.filter(pk=41)
    print(pos45)


    context = {
        'title': 'Посты по тегам',
        'posts': posts,
        'image': image,
        'tag': tags,
        'name_tag': name_tag,
    }
    return render(request, 'publication_app/tag.html', context)

"""    
from django.db.models import Count
#область тегов. Анотация выполняет суммирование по использованным тегам, сортирует их и выводит 5 популярных
    coun = Tag.objects.annotate(cnt=Count('post')).order_by('-cnt')[:5]
    for i in coun:
        print(i.tag, i.cnt, )
"""