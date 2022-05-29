from rest_framework import serializers
from tag_app.models import Hashtag


class HashtagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hashtag
        fields = '__all__'
        read_only_fields = ('id',)