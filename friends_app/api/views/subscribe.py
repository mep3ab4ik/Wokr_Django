from rest_framework.mixins import CreateModelMixin, ListModelMixin, DestroyModelMixin
from rest_framework.viewsets import GenericViewSet

from ..serializers.subscribe import SubscribeSerializer
from ...models import Friendship


class SubscribeViewSet(GenericViewSet, ListModelMixin, CreateModelMixin, DestroyModelMixin):
    """
    Метод GET показывает все поля подписчиков. Кто отправитель и принимающий.

    Метод POST отправляет запрос в подписки по id. Если пользователь только ПОДПИСЫВАЕТСЯ(без добавления в друзей)
    Для этого поле "wait_answer" ставим в положение False.

    Метод Destroy принимает pk записи с модели Friendship для удаления с бд.
    """
    serializer_class = SubscribeSerializer
    queryset = Friendship.objects.filter(is_sub=True, wait_answer=False)