from rest_framework import serializers

from ...models import Friendship


class FriendshipSerializer(serializers.ModelSerializer):
    class Meta:
        model = Friendship
        fields = ['sender', 'receiver', 'publisher_sender']
        read_only_fields = ['sender']

    publisher_sender = serializers.HiddenField(
        default=serializers.CurrentUserDefault(),
        source='sender',
    )


class UpdateFriendshipSerializer(serializers.ModelSerializer):
    class Meta:
        model = Friendship
        fields = "__all__"
        read_only_fields = ['receiver']

    publisher_receiver = serializers.HiddenField(
        default=serializers.CurrentUserDefault(),
        source='receiver',
    )
