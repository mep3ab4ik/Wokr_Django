from django.shortcuts import render
from django.views import View
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User


class ProfileUserView(View):

    @staticmethod
    def get(request, pk):
        users = get_object_or_404(User, pk=pk)
        context = {
            'title': f'Профиль {users.username}',
            'users': users,
        }
        return render(request, 'profile_app/profileuser.html', context)

    # @staticmethod
    # def post(request, pk):
    #     pass
    #     # new_request = request.POST.copy()
    #     # new_request['user'] = request.user.pk
    #     # new_request['post'] = pk
    #     # print(new_request)
    #     # form = AddCommentsForm(data=new_request)
    #     # if form.is_valid:
    #     #     form.save()
    #     #     return redirect(f'/post/{pk}')