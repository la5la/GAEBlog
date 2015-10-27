from django.conf.urls import patterns, include, url

import session_csrf

session_csrf.monkeypatch()

from django.contrib import admin

admin.autodiscover()

from django.views.decorators.cache import cache_page
from blog.views import IndexView
from blog.views import PostView

urlpatterns = patterns('',
                       # Examples:
                       url(r'^$', view=IndexView.as_view(), name='index', kwargs={"page_num": "1"}),
                       # url(r'^$', cache_page(24*60*60)(IndexView.as_view()), name='index'),
                       url(r'^page/(?P<page_num>[0-9]+)/$', IndexView.as_view(), name='page'),
                       # url(r'^(?P<year>[0-9]{4})/(?P<month>[0-9]{2})/(?P<day>[0-9]{2})/(?P<url_slug>[\w\W]+)/$', cache_page(24*60*60)(PostView.as_view()), name='post'),
                       url(r'^(?P<year>[0-9]{4})/(?P<month>[0-9]{2})/(?P<day>[0-9]{2})/(?P<url_slug>[\w\W]+)/$', PostView.as_view(), name='post'),
                       # url(r'^blog/', include('blog.urls')),
                       url(r'^_ah/', include('djangae.urls')),

                       # Note that by default this is also locked down with login:admin in app.yaml
                       url(r'^admin/', include(admin.site.urls)),

                       # url(r'^csp/', include('cspreports.urls')),

                       url(r'^auth/', include('djangae.contrib.gauth.urls')),
                       )
