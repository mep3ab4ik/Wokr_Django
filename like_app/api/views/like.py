from rest_framework import filters
from rest_framework.mixins import RetrieveModelMixin, CreateModelMixin, ListModelMixin
from rest_framework.viewsets import GenericViewSet
from ..serializers.like import LikeSerializer
from ...models import Like


class LikeView(GenericViewSet, ListModelMixin, CreateModelMixin):
    serializer_class = LikeSerializer
    queryset = Like.objects.all()
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ['created_time']