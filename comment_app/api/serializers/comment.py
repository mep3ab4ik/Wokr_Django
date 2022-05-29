from rest_framework import serializers
from ...models import Comment
from like_app.api.serializers.like import LikeSerializer


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = "__all__"
        read_only_fields = ['user']

    publisher_user = serializers.HiddenField(
        default=serializers.CurrentUserDefault(),
        source='user',
    )

    likes = LikeSerializer(source='com_like', many=True, read_only=True)