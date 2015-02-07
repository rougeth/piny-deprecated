from collections import OrderedDict

from django.core.urlresolvers import reverse
from rest_framework.test import APITestCase
from model_mommy import mommy

from core.models import Url


class ShorteningUrl(APITestCase):

    def setUp(self):
        url = 'https://pi.ny'
        self.data = {
            'original_url': url,
            'custom_shortened_url': None
        }
        self.response = self.client.post(reverse('api_url_list_create'),
                                         self.data)

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


class ListingUrls(APITestCase):

    def setUp(self):
        self.data = mommy.make(Url, _quantity=3)
        self.response = self.client.get(reverse('api_url_list_create'))

    def test_status_code(self):
        self.assertEqual(self.response.status_code, 200)

    def test_data(self):
        self.assertEqual(len(self.response.data), 3)
        # to-do: test self.response.data content
