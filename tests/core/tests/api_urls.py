from django.conf.urls.defaults import patterns, include, url
from core.tests.api import Api, NoteResource, UserResource


api = Api()
api.register(NoteResource())
api.register(UserResource())

urlpatterns = patterns('',
    url(r'^api/', include(api.urls)),
)
