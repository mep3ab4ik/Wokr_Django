from rest_framework import serializers
from publication_app.models import Post
from media_app.api.serializers.media import MedialSerializer
from comment_app.api.serializers.comment import CommentSerializer


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        exclude = ['is_public']
        read_only_fields = ('id', 'user')
        extra_kwargs = {
            'file': {
                'required': True,
                'write_only': True,
                'help_text': 'ID media file',
            },
            # 'comment': {
            #     'required': True,
            #     'write_only': True,
            #     'help_text': 'Com into Post'
            # },
        }


    publisher_user = serializers.HiddenField(
        default=serializers.CurrentUserDefault(),
        source='user',
    )
    # media = serializers.URLField(source='file.file.url', read_only=True)
    media = MedialSerializer(source='file', allow_null=True, read_only=True)
    comment = CommentSerializer(allow_null=True, read_only=True)
