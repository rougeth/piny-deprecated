from django.conf.urls import patterns, url

from core.views import HomeView, UrlRedirectView


urlpatterns = patterns(
    '',
    url(r'^login$', 'django.contrib.auth.views.login',
        {'template_name': 'core/login.html'}, name='login'),
    url(r'^logout$', 'django.contrib.auth.views.logout', {'next_page': '/'},
        name='logout'),
    url(r'^$', HomeView.as_view(), name='home'),
    url(r'^(?P<url_code>\w+)$', UrlRedirectView.as_view(),
        name='url_redirect_view'),
)
