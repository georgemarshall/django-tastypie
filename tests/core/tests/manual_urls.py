from django.conf.urls.defaults import patterns, include, url
from core.tests.resources import NoteResource


note_resource = NoteResource()

urlpatterns = patterns('',
    url(r'^', include(note_resource.urls)),
)
