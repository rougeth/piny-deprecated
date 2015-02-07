from rest_framework import generics, serializers, status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from core.models import Url


class UrlSerializer(serializers.ModelSerializer):
    class Meta:
        model = Url
        fields = ('original_url', 'custom_shortened_url',)


class CreateUrl(generics.CreateAPIView):
    serializer_class = UrlSerializer


@api_view(['POST'])
def create_url(request):
    serializer = UrlSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
