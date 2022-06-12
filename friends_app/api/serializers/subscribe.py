from rest_framework import serializers

from ...models import Friendship


class SubscribeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Friendship
        fields = ['sender', 'receiver', 'publisher_sender', 'wait_answer']
        read_only_fields = ['sender']

    publisher_sender = serializers.HiddenField(
        default=serializers.CurrentUserDefault(),
        source='sender',
    )
