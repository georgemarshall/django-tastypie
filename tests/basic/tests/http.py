from django.test.testcases import TestCase

from django.utils import simplejson as json
from django.utils import unittest
from tastypie.serializers import lxml, yaml, biplist


class HTTPTestCase(TestCase):
    def test_get_apis_json(self):
        response = self.client.get('/api/v1/', HTTP_ACCEPT='application/json')
        self.assertContains(response, '{"notes": {"list_endpoint": "/api/v1/notes/", "schema": "/api/v1/notes/schema/"}, "users": {"list_endpoint": "/api/v1/users/", "schema": "/api/v1/users/schema/"}}')

    @unittest.skipUnless(lxml, 'lxml not installed')
    def test_get_apis_xml(self):
        response = self.client.get('/api/v1/', HTTP_ACCEPT='application/xml')
        self.assertContains(response, '<?xml version=\'1.0\' encoding=\'utf-8\'?>\n<response><notes type="hash"><list_endpoint>/api/v1/notes/</list_endpoint><schema>/api/v1/notes/schema/</schema></notes><users type="hash"><list_endpoint>/api/v1/users/</list_endpoint><schema>/api/v1/users/schema/</schema></users></response>')

    @unittest.skipUnless(yaml, 'yaml not installed')
    def test_get_apis_yaml(self):
        response = self.client.get('/api/v1/', HTTP_ACCEPT='text/yaml')
        self.assertContains(response, "notes: {list_endpoint: !!python/unicode '/api/v1/notes/', schema: !!python/unicode '/api/v1/notes/schema/'}\nusers: {list_endpoint: !!python/unicode '/api/v1/users/', schema: !!python/unicode '/api/v1/users/schema/'}\n")

    @unittest.skipUnless(biplist, 'biplist not installed')
    def test_get_apis_plist(self):
        response = self.client.get('/api/v1/', HTTP_ACCEPT='application/x-plist')
        self.assertContains(response, 'bplist00bybiplist1.0\x00\xd2\x01\x02\x03\x04UnotesUusers\xd2\x05\x06\x07\x08]list_endpointVscheman\x00/\x00a\x00p\x00i\x00/\x00v\x001\x00/\x00n\x00o\x00t\x00e\x00s\x00/o\x10\x15\x00/\x00a\x00p\x00i\x00/\x00v\x001\x00/\x00n\x00o\x00t\x00e\x00s\x00/\x00s\x00c\x00h\x00e\x00m\x00a\x00/\xd2\x05\x06\t\nn\x00/\x00a\x00p\x00i\x00/\x00v\x001\x00/\x00u\x00s\x00e\x00r\x00s\x00/o\x10\x15\x00/\x00a\x00p\x00i\x00/\x00v\x001\x00/\x00u\x00s\x00e\x00r\x00s\x00/\x00s\x00c\x00h\x00e\x00m\x00a\x00/\x15\x1a &\x8a+9@]\x8f\xac\x00\x00\x00\x00\x00\x00\x01\x01\x00\x00\x00\x00\x00\x00\x00\x0b\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xd9')

    def test_get_list(self):
        response = self.client.get('/api/v1/notes/', HTTP_ACCEPT='application/json')
        self.assertContains(response, '{"meta": {"limit": 20, "next": null, "offset": 0, "previous": null, "total_count": 2}, "objects": [{"content": "This is my very first post using my shiny new API. Pretty sweet, huh?", "created": "2010-03-30T20:05:00", "id": "1", "is_active": true, "resource_uri": "/api/v1/notes/1/", "slug": "first-post", "title": "First Post!", "updated": "2010-03-30T20:05:00", "user": "/api/v1/users/1/"}, {"content": "The dog ate my cat today. He looks seriously uncomfortable.", "created": "2010-03-31T20:05:00", "id": "2", "is_active": true, "resource_uri": "/api/v1/notes/2/", "slug": "another-post", "title": "Another Post", "updated": "2010-03-31T20:05:00", "user": "/api/v1/users/1/"}]}')

    def test_post_object(self):
        post_data = '{"content": "A new post.", "is_active": true, "title": "New Title", "slug": "new-title", "user": "/api/v1/users/1/"}'
        response = self.client.post('/api/v1/notes/', data=post_data, content_type='application/json', HTTP_ACCEPT='application/json')
        self.assertRedirects(response, '/api/v1/notes/3/', 201)

        # make sure posted object exists
        response = self.client.get('/api/v1/notes/3/', HTTP_ACCEPT='application/json')
        self.assertContains(response, '')

        obj = json.loads(response.content)
        self.assertEqual(obj['content'], 'A new post.')
        self.assertEqual(obj['is_active'], True)
        self.assertEqual(obj['user'], '/api/v1/users/1/')
