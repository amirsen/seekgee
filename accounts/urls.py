from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('accounts.views',
                        url(r'^profile/$', 'profile'),
)
                       
