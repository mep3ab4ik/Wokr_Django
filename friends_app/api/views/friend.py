from rest_framework.mixins import RetrieveModelMixin, CreateModelMixin, ListModelMixin, UpdateModelMixin
from rest_framework.viewsets import GenericViewSet

from ..serializers.friend import FriendshipSerializer
from ...models import Friendship


class FriendshipViewSet(GenericViewSet, RetrieveModelMixin,ListModelMixin, UpdateModelMixin, CreateModelMixin):
    serializer_class = FriendshipSerializer
    queryset = Friendship.objects.all()