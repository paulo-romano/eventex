from django.test import TestCase
from django.core.signals import Signal
from eventex.subscriptions.signals import subscription_created


class SignalsTest(TestCase):
    def test_subscription_created_signal(self):
        """Must have a subscription created signal"""
        self.assertIsInstance(subscription_created, Signal)

    def test_subscription_created_signal_param(self):
        """Subscription created signal must have name param"""
        self.assertIn('name', subscription_created.providing_args)