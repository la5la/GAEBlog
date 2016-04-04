from django.conf.urls import patterns, include, url

import session_csrf

session_csrf.monkeypatch()

from django.contrib import admin

admin.autodiscover()

from blog.views import index
from blog.views import post
from blog.views import sitemap

urlpatterns = patterns('',
                       # Examples:
                       url(r'^$', index, name='index'),
                       url(r'^(?P<year>[0-9]{4})/(?P<month>[0-9]{2})/(?P<day>[0-9]{2})/(?P<url_slug>[\w\W]+)/$', post, name='post'),
                       url(r'^sitemap\.xml/$', sitemap, name='sitemap'),
                       url(r'^_ah/', include('djangae.urls')),
                       url(r'^admin/', include(admin.site.urls)),
                       url(r'^auth/', include('djangae.contrib.gauth.urls')),
                       )
