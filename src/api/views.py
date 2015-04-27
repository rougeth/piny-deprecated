from rest_framework.generics import ListCreateAPIView

from core.models import Url
from api.serializers import UrlSerializer


class UrlListCreate(ListCreateAPIView):
    queryset = Url.objects.all()
    serializer_class = UrlSerializer
