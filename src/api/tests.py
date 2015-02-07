from django.core.urlresolvers import reverse

from rest_framework.test import APITestCase


class ShorteningUrl(APITestCase):

    def setUp(self):
        url = 'https://pi.ny'
        self.data = {
            'original_url': url,
            'custom_shortened_url': None
        }
        self.response = self.client.post(reverse('api_create_url'), self.data)

    def test_status_code(self):
        # 201 Created: The request has been fulfilled and resulted in a new
        # resource being created
        self.assertEqual(self.response.status_code, 201)

    def test_data(self):
        data = {}
        for (key, value) in self.data.items():
            # response.data returns a dict with string keys and values
            data[key] = str(value)

        self.assertEqual(self.response.data, data)

    def test_get_request(self):
        response = self.client.get(reverse('api_create_url'), self.data)
        # 405 Method Not Allowed: A request was made of a resource using a
        # request method not supported by that resource
        self.assertEqual(response.status_code, 405)
