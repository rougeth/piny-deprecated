from django.conf.urls import patterns, url

from api.views import CreateUrl

urlpatterns = patterns(
    'api.views',
    url(r'^create/url$', CreateUrl.as_view(), name='api_create_url'),
)
