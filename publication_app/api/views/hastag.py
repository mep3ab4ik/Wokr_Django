from rest_framework.mixins import ListModelMixin
from rest_framework.viewsets import GenericViewSet

from ..serializers.hashtag import HashtagSerializer
from tag_app.models import Hashtag


class HashtagView(GenericViewSet, ListModelMixin):
    serializer_class = HashtagSerializer
    queryset = Hashtag.objects.all()


