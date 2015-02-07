from rest_framework import serializers
from core.models import Url


class UrlSerializer(serializers.ModelSerializer):
    class Meta:
        model = Url
        fields = ('original_url', 'custom_shortened_url',)
