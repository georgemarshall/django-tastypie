from __future__ import absolute_import

from django.conf.urls.defaults import patterns, include, url
from tastypie.api import Api

from .resources import NoteResource, UserResource


api = Api(api_name='v1')
api.register(NoteResource(), canonical=True)
api.register(UserResource(), canonical=True)

urlpatterns = patterns('',
    url(r'^api/', include(api.urls)),
)
