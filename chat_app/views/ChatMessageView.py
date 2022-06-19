from django.db.models import Q
from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.models import User

from ..forms.ChatMessageForm import ChatMessageForm
from ..models import Chat


class ChatMessageView(View):

    @staticmethod
    def get(request, pk):
        # Получаем текс чата и сортируем по pk
        message = Chat.objects.filter(
            (Q(sender=pk) & Q(recipient=request.user.pk)) |
            (Q(sender=request.user.pk) & Q(recipient=pk))
        ).order_by("pk")

        form = ChatMessageForm()
        context = {
            'title': f'Чат с пользователем ',
            'message': message,
            'form': form,
        }
        return render(request, 'chat_app/chat.html', context)

    @staticmethod
    def post(request, pk):
        new_request = request.POST.copy()
        new_request['sender'] = request.user.pk
        new_request['recipient'] = (User.objects.get(pk=pk)).pk
        # print(new_request)

        form = ChatMessageForm(new_request)
        if form.is_valid():
            form.save()
            return redirect(f'/message/{pk}')




