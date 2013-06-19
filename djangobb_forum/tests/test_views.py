from django.core.urlresolvers import reverse
from django.test import TestCase


class TestViews(TestCase):
    fixtures = ['test_forum.json']

    def test_djangobb_index(self):
        self.client.get(reverse('djangobb_index'))

    def test_djangobb_index(self):
        self.client.get(reverse('djangobb_forum'))

    def test_djangobb_index(self):
        self.client.get(reverse('djangobb_moderate'))

    def test_djangobb_index(self):
        self.client.get(reverse('djangobb_search'))

    def test_djangobb_index(self):
        self.client.get(reverse('djangobb_misc'))