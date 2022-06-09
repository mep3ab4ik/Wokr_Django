from rest_framework import serializers

from ...models import Friendship


class FriendshipSerializer(serializers.ModelSerializer):
    class Meta:
        model = Friendship
        fields = ['sender', 'receiver']
        read_only_fields = ['sender']

    publisher_user = serializers.HiddenField(
        default=serializers.CurrentUserDefault(),
        source='sender',
    )
