from __future__ import absolute_import

from django.conf.urls.defaults import patterns, include, url
from tastypie.api import NamespacedApi

from .resources import NamespacedNoteResource, NamespacedUserResource


api = NamespacedApi(api_name='v1', urlconf_namespace='special')
api.register(NamespacedNoteResource(), canonical=True)
api.register(NamespacedUserResource(), canonical=True)

urlpatterns = patterns('',
    url(r'^api/', include(api.urls, namespace='special')),
)
