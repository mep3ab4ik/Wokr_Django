from rest_framework.mixins import CreateModelMixin, ListModelMixin
from rest_framework.viewsets import GenericViewSet
from ..serializers.chat import ChatSerializer
from ...models import Chat


class ChatView(GenericViewSet, ListModelMixin, CreateModelMixin):
    serializer_class = ChatSerializer
    queryset = Chat.objects.all()
