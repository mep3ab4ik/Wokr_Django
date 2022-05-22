from rest_framework import serializers
from publication_app.models import Post
from tag_app.models import Hashtag


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'
        read_only_fields = ('id', 'user')


    publisher_user = serializers.HiddenField(
        default=serializers.CurrentUserDefault(),
        source='user',
    )


class HashtagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hashtag
        fields = '__all__'
        read_only_fields = ('id',)