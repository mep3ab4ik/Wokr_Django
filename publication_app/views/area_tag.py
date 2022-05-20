from django.views import View
from django.shortcuts import render
from tag_app.models import Tag, Hashtag
from django.db.models import Count


class Tags(View):

    @staticmethod
    def get(request):
        # область тегов. Анотация выполняет суммирование по использованным тегам, сортирует их и выводит 5 популярных
        count_hashtag = Hashtag.objects.annotate(cnt=Count('hashtagpost')).order_by('-cnt')[:7]
        count_tag = Tag.objects.annotate(cnt=Count('post')).order_by('-cnt')

        context = {
            'title': 'Область тегов',
            'tag': count_tag,
            'hashtags': count_hashtag,
        }
        return render(request, 'publication_app/area_tag.html', context)


