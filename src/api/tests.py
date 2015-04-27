from django.test import TestCase
from model_mommy import mommy

from core.models import Url


class TestUrlListCreate(TestCase):

    def setUp(self):
        mommy.make(Url, _quantity=5)
        self.response = self.client.get('/api/url')

    def test_status_code(self):
        self.assertEqual(self.response.status_code, 200)

    def test_quantity_of_urls(self):
        self.assertEqual(len(self.response.data), 5)
