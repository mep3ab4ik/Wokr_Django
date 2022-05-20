from django.views import View
from django.shortcuts import render
from tag_app.models import Tag, Hashtag
from django.db.models import Count

"""    
from django.db.models import Count
#область тегов. Анотация выполняет суммирование по использованным тегам, сортирует их и выводит 5 популярных
    coun = Tag.objects.annotate(cnt=Count('post')).order_by('-cnt')[:5]
    for i in coun:
        print(i.tag, i.cnt, )
"""


class Tags(View):

    @staticmethod
    def get(request):
        count_hashtag = Hashtag.objects.annotate(cnt=Count('hashtagpost')).order_by('-cnt')[:5]
        count_tag = Tag.objects.annotate(cnt=Count('post')).order_by('-cnt')
        

