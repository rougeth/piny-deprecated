from rest_framework import generics

from api.serializers import UrlSerializer
from core.models import Url


class UrlListCreate(generics.ListCreateAPIView):
    queryset = Url.objects.all()
    serializer_class = UrlSerializer
