from django.shortcuts import render
from django.views import View
from django.views.generic import ListView
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from django.shortcuts import render
from django.db.models import Q

# Create your views here.


class UserSearchListView(ListView):
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
            return queryset.filter(Q(username__icontains=q))
        return None

# class UserSearchView(View):
#     def get(self, request):
#         # print(dir(request))
#         # print(request.GET)
#         query = request.GET.get('q')
#         contex = {
#         }
#         return render(request, "search_app/search.html", contex)