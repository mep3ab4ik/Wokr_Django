from rest_framework.mixins import CreateModelMixin, ListModelMixin, UpdateModelMixin
from rest_framework.viewsets import GenericViewSet

from ..serializers.friend import FriendshipSerializer, UpdateFriendshipSerializer
from ...models import Friendship


class FriendsViewSet(GenericViewSet, ListModelMixin, CreateModelMixin):
    """
    Метод GET показывает всех друзей. Кто отправитель и принимающий.
    Метод POST отправляет запрос в друзья по id. Больше ничего не нужно
    """
    serializer_class = FriendshipSerializer
    queryset = Friendship.objects.filter(is_accepted=True)


class UpdateFriendsViewSet(GenericViewSet, UpdateModelMixin):
    """
    Через обновление происходит удаление их друзей.
    Когда пользователь удаляет друга, то в базе данных поле "is_accepted" переходит в Fasle.
    Если "пользователя", который принял дружбу удаляю, то передаем обновляем поле sender c его id.
    """
    serializer_class = UpdateFriendshipSerializer
    queryset = Friendship.objects.filter(is_accepted=True)


class SubscribeViewSet(GenericViewSet, ListModelMixin, UpdateModelMixin, CreateModelMixin):
    serializer_class = FriendshipSerializer
    queryset = Friendship.objects.filter(is_sub=True)