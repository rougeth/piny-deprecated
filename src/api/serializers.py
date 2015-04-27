from rest_framework import serializers

from core.models import Url


class UrlSerializer(serializers.ModelSerializer):
    class Meta:
        model = Url
        fields = ('id', 'original_url', 'custom_url')
