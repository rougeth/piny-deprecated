from django.conf.urls import patterns, url

from api.views import UrlListCreate


urlpatterns = patterns(
    'api.views',
    url(r'^url$', UrlListCreate.as_view(), name='api_url_list_create'),
)
