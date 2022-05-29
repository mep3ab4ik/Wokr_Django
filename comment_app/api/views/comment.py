from rest_framework import filters
from rest_framework.mixins import RetrieveModelMixin, CreateModelMixin, ListModelMixin
from rest_framework.viewsets import GenericViewSet
from ..serializers.comment import CommentSerializer
from ...models import Comment


class CommentView(GenericViewSet, RetrieveModelMixin,ListModelMixin, CreateModelMixin):
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ['created_time']