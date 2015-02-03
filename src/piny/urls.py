from django.conf.urls import patterns, include, url
from django.contrib import admin

from core.views import HomeView

urlpatterns = patterns(
    '',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^login$', 'django.contrib.auth.views.login',
        {'template_name': 'core/login.html'}, name='login'),
    url(r'^logout$', 'django.contrib.auth.views.logout', {'next_page': '/'},
        name='logout'),
    url(r'^$', HomeView.as_view(), name='home'),
)
