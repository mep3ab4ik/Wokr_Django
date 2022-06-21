from django.views import View
from django.shortcuts import render
from django.db.models import Count


from tag_app.models import Tag, Hashtag


class Tags(View):
    """View области тегов"""
    @staticmethod
    def get(request):
        # Область тегов.
        # Аннотация выполняет суммирование по использованным тегам, сортирует их и выводит 7 популярных
        count_hashtag = Hashtag.objects.annotate(cnt=Count('hashtagpost')).order_by('-cnt')[:7]

        # Получаем теги и их количество
        count_tag = Tag.objects.annotate(cnt=Count('tag_post')).order_by('-cnt')

        context = {
            'title': 'Область тегов',
            'tag': count_tag,
            'hashtags': count_hashtag,
        }
        return render(request, 'publication_app/area_tag.html', context)


