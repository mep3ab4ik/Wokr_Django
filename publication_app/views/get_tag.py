from django.core.paginator import Paginator
from django.shortcuts import render
from django.views import View
from django.views.generic import ListView

from tag_app.models import Tag
from publication_app.models import Post


class GetTag(ListView):
    queryset = Post.objects.all()
    template_name = 'profile_app/main_page.html'
    paginate_by = 3
    context_object_name = 'posts'

    def get_queryset(self):
        return Post.objects.filter(tag__tag=self.kwargs['tag'])

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)
        context['title'] = f"Посты по тегу {self.kwargs['tag']}"
        context['name_text'] = context['title']
        context['tag'] = Tag.objects.all()
        return context

# class GetTag(View):
#     """
#     View получение тегов и перехожу к постам по тегу
#     """
#     @staticmethod
#     def get(request, tag):
#         # Получаем тег на который перешел пользователь
#         our_tag = Tag.objects.get(tag=tag)
#
#         # Получаем все теги
#         tags = Tag.objects.all()
#
#         # Получаем посты по определённому тегу
#         posts = Post.objects.filter(tag=our_tag)
#
#         # Пагинация Queryset по 3 объекта на страницу
#         paginator = Paginator(posts, 3)
#         # Получаем номер страницы
#         page_number = request.GET.get('page')
#         # Получаем объект
#         page_obj = paginator.get_page(page_number)
#
#         context = {
#             'title': 'Посты по тегам',
#             'name_text': f'Публикации по тегу "{our_tag.tag.tag}"',
#             'posts': page_obj,
#             'tag': tags,
#             'name_tag': our_tag.tag,
#         }
#         return render(request, 'profile_app/main_page.html', context)


