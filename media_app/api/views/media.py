from rest_framework.mixins import RetrieveModelMixin, CreateModelMixin
from rest_framework.viewsets import GenericViewSet

from ..serializers.media import MedialSerializer
from ...models import Media


class MediaViewSet(GenericViewSet, RetrieveModelMixin, CreateModelMixin):
    serializer_class = MedialSerializer
    queryset = Media.objects.all()