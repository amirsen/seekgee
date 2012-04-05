from django.conf.urls.defaults import patterns, include, url
from django.views.generic import DetailView
from qaa.models import Question

urlpatterns = patterns('',
                       url(r'^$', 'qaa.views.index'),
                       url(r'^(?P<pk>\d+)/$',
                           DetailView.as_view(
            model=Question)),
                       url(r'^ask/$', 'qaa.views.ask'),
                       url(r'^ask/submit/$', 'qaa.views.submit'),
)
