from django.views.generic import ListView
from django.contrib.auth.models import User
from django.db.models import Q


class UserSearchListView(ListView):
    """View поиска пользователей"""

    model = User
    queryset = User.objects.all()
    template_name = "search_app/search.html"
    context_object_name = "searchlists"

    def get_queryset(self):
        # Получаем не отфильтрованный кверисет всех моделей
        queryset = super(UserSearchListView, self).get_queryset()
        q = self.request.GET.get("q")

        if q:
            # Если 'q' в GET запросе, фильтруем кверисет по данным из 'q'
            # Для поиска пользователей у которых есть такое в имени.
            # return queryset.filter(Q(username__icontains=q)).
            # Для поиска пользователей у которых начинается имя.
            return queryset.filter(Q(username__startswith=q))
        return None

