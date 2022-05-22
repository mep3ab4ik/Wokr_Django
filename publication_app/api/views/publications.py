from rest_framework import filters, generics
from rest_framework.mixins import ListModelMixin, CreateModelMixin
from rest_framework.viewsets import GenericViewSet
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.pagination import LimitOffsetPagination

from ..serializers.publications import PostSerializer, HashtagSerializer
from publication_app.models import Post
from tag_app.models import Hashtag, Tag


class PostView(GenericViewSet, ListModelMixin, CreateModelMixin):
    serializer_class = PostSerializer
    queryset = Post.objects.all()
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ['created_time']

    # @action(methods=['get'], detail=False)
    # def tag(self, request):
    #     tag = Tag.objects.all()
    #     return Response(tag)



class HashtagView(GenericViewSet, ListModelMixin):
    serializer_class = HashtagSerializer
    queryset = Hashtag.objects.all()


class TagPagination(LimitOffsetPagination):
    """ Клас собственной пагинации.
    Если нам нужна другая пагинация для определённых классов, то исползуем данные вариант """
    default_limit = 2
    offset_query_param = "offset"
    limit_query_param = 'limit'
    max_limit = 10000000



class TagPostView(APIView, LimitOffsetPagination):
    """Поиск постов по определённым тегам.

    В поля вводим Тэг для поиска. Надо узнать как сделать выпадающий список???????
    """

    def get(self, request, tag):
        tag = Tag.objects.get(tag=tag)
        post = Post.objects.filter(tag__id=tag.pk)
        results = self.paginate_queryset(queryset=post, request=request, view=self)
        serializer = PostSerializer(instance=results, many=True)
        return Response(serializer.data)



class HashtagPostView(APIView, LimitOffsetPagination):
    """Поиск постов по хэштегам.

    Вводим #текс и выдает посты, где были такие хэштеги.
    """

    def get(self, request, hashtag):
        hashtag = Hashtag.objects.get(hashtag=hashtag)
        post = Post.objects.filter(hashtag_post__hashtag=hashtag)
        # Используем пагинацию, которую добавлил в settings
        results = self.paginate_queryset(queryset=post, request=request, view=self)
        serializer = PostSerializer(instance=results, many=True)
        return Response(serializer.data)