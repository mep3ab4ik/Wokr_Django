from rest_framework.mixins import RetrieveModelMixin, CreateModelMixin
from rest_framework.viewsets import GenericViewSet

from ..serializers.friend import FriendshipSerializer
from ...models import Friendship


class MediaViewSet(GenericViewSet, RetrieveModelMixin, CreateModelMixin):
    serializer_class = MedialSerializer
    queryset = Media.objects.all()