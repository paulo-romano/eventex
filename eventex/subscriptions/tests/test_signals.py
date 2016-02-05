from django.shortcuts import resolve_url
from django.test import TestCase
from django.core.signals import Signal
from eventex.subscriptions.signals import subscription_created
from unittest.mock import Mock

from eventex.subscriptions.views import create


class SignalsTest(TestCase):
    def setUp(self):
        self.data = dict(name='Paulo Romano', cpf='12345678901',
            email='pauloromanocarvalho@gmail.com', phone='11-55556666')

    def test_subscription_created_signal(self):
        """Must have a subscription created signal"""
        self.assertIsInstance(subscription_created, Signal)

    def test_subscription_created_signal_param(self):
        """Subscription created signal must have name param"""
        self.assertIn('name', subscription_created.providing_args)

    def test_subscription_created_call(self):
        """Subscription created signal must be called with some name in subscriptions:new"""
        mock = Mock()
        subscription_created.connect(mock)

        self.make_subscription()

        mock.assert_called_with(name=self.data.get('name'), sender=create, signal=subscription_created)

    def make_subscription(self):
        return self.client.post(resolve_url('subscriptions:new'), self.data)