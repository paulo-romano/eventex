from django.test import TestCase
from django.shortcuts import resolve_url


class HomeTest(TestCase):
    def setUp(self):
        self.response = self.client.get(resolve_url('home'))

    def test_get(self):
        """GET / Must return status code 200"""
        self.assertEqual(200, self.response.status_code)

    def test_template(self):
        """Must use index.html template"""
        self.assertTemplateUsed(self.response, 'index.html')

    def test_subscription_link(self):
        """Must have link to subscription"""
        expected = 'href="{0}"'.format(resolve_url('subscriptions:new'))
        self.assertContains(self.response, expected)
