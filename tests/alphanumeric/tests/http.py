from django.test.testcases import TestCase
from django.utils import simplejson as json, unittest
from tastypie.serializers import lxml, yaml, biplist

class HTTPTestCase(TestCase):
    def test_get_apis_json(self):
        response = self.client.get('/api/v1/', HTTP_ACCEPT='application/json')
        self.assertContains(response, '{"products": {"list_endpoint": "/api/v1/products/", "schema": "/api/v1/products/schema/"}}')

    @unittest.skipUnless(lxml, 'lxml not installed')
    def test_get_apis_xml(self):
        response = self.client.get('/api/v1/', HTTP_ACCEPT='application/xml')
        self.assertContains(response, '<?xml version=\'1.0\' encoding=\'utf-8\'?>\n<response><products type="hash"><list_endpoint>/api/v1/products/</list_endpoint><schema>/api/v1/products/schema/</schema></products></response>')

    @unittest.skipUnless(yaml, 'yaml not installed')
    def test_get_apis_yaml(self):
        response = self.client.get('/api/v1/', HTTP_ACCEPT='text/yaml')
        self.assertContains(response, "products: {list_endpoint: !!python/unicode '/api/v1/products/', schema: !!python/unicode '/api/v1/products/schema/'}\n")

    @unittest.skipUnless(biplist, 'biplist not installed')
    def test_get_apis_plist(self):
        response = self.client.get('/api/v1/', HTTP_ACCEPT='application/x-plist')
        self.assertContains(response, 'bplist00bybiplist1.0\x00\xd1\x01\x02Xproducts\xd2\x03\x04\x05\x06]list_endpointVschemao\x10\x11\x00/\x00a\x00p\x00i\x00/\x00v\x001\x00/\x00p\x00r\x00o\x00d\x00u\x00c\x00t\x00s\x00/o\x10\x18\x00/\x00a\x00p\x00i\x00/\x00v\x001\x00/\x00p\x00r\x00o\x00d\x00u\x00c\x00t\x00s\x00/\x00s\x00c\x00h\x00e\x00m\x00a\x00/\x15\x18!&4;`\x00\x00\x00\x00\x00\x00\x01\x01\x00\x00\x00\x00\x00\x00\x00\x07\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x93')

    def test_get_list(self):
        expected = {
            'meta': {
                'previous': None,
                'total_count': 6,
                'offset': 0,
                'limit': 20,
                'next': None
            },
            'objects': [
                {
                    'updated': '2010-03-30T20:05:00',
                    'resource_uri': '/api/v1/products/11111/',
                    'name': 'Skateboardrampe',
                    'artnr': '11111',
                    'created': '2010-03-30T20:05:00'
                },
                {
                    'updated': '2010-05-04T20:05:00',
                    'resource_uri': '/api/v1/products/76123/',
                    'name': 'Bigwheel',
                    'artnr': '76123',
                    'created': '2010-05-04T20:05:00'
                },
                {
                    'updated': '2010-05-04T20:05:00',
                    'resource_uri': '/api/v1/products/WS65150-01/',
                    'name': 'Trampolin',
                    'artnr': 'WS65150-01',
                    'created': '2010-05-04T20:05:00'
                },
                {
                    'updated': '2010-05-04T20:05:00',
                    'resource_uri': '/api/v1/products/65100A-01/',
                    'name': 'Laufrad',
                    'artnr': '65100A-01',
                    'created': '2010-05-04T20:05:00'
                },
                {
                    'updated': '2010-05-04T20:05:00',
                    'resource_uri': '/api/v1/products/76123/01/',
                    'name': 'Bigwheel',
                    'artnr': '76123/01',
                    'created': '2010-05-04T20:05:00'
                },
                {
                    'updated': '2010-05-04T20:05:00',
                    'resource_uri': '/api/v1/products/WS65150/01-01/',
                    'name': 'Trampolin',
                    'artnr': 'WS65150/01-01',
                    'created': '2010-05-04T20:05:00'
                }
            ]
        }
        response = self.client.get('/api/v1/products/', HTTP_ACCEPT='application/json')
        self.assertContains(response, '')
        self.assertEqual(json.loads(response.content), expected)

    def test_post_object(self):
        post_data = '{"artnr": "A76124/03", "name": "Bigwheel XXL"}'
        response = self.client.post('/api/v1/products/', data=post_data, content_type='application/json', HTTP_ACCEPT='application/json')
        self.assertRedirects(response, '/api/v1/products/A76124/03/', 201)

        # make sure posted object exists
        response = self.client.get('/api/v1/products/A76124/03/', HTTP_ACCEPT='application/json')
        self.assertContains(response, '')

        obj = json.loads(response.content)

        self.assertEqual(obj['name'], 'Bigwheel XXL')
        self.assertEqual(obj['artnr'], 'A76124/03')
