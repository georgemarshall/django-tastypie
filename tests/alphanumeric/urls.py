from django.conf.urls.defaults import patterns, include, url

urlpatterns = patterns('',
    url(r'^api/', include('alphanumeric.api.urls')),
)
