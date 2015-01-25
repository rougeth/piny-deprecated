from django.conf.urls import patterns, include, url
from django.contrib import admin

from core.views import HomeView

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'piny.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^login$', 'django.contrib.auth.views.login', { 'template_name':
        'core/login.html' }, name='login'),
    url(r'^$', HomeView.as_view(), name='home'),
)
