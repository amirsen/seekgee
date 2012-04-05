from django.conf.urls.defaults import patterns, include, url
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.core.urlresolvers import reverse

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'seekgee.views.home', name='home'),
    # url(r'^seekgee/', include('seekgee.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
                           url(r'^login/', 'django.contrib.auth.views.login',
                               {'template_name': 'accounts/login.html'}),
                       url(r'^logout/$', 'django.contrib.auth.views.logout', {'next_page': '/',}),
                       url(r'^$', 'main.views.index'),
                       url(r'^questions/', include('qaa.urls')),
                       url(r'^admin/', include(admin.site.urls)),
                       url(r'^media/(?P<path>.*)$', 'django.views.static.serve',
                           {'document_root': settings.MEDIA_ROOT}),
                       url(r'^accounts/', include('accounts.urls')),
                       )
urlpatterns += staticfiles_urlpatterns()
