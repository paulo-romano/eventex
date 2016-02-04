from django.test import TestCase
from django.core.signals import Signal


class SignalsTest(TestCase):
    def test_subscription_created_signal(self):
        """Must have a subscription created signal"""
        self.assertIsInstance(subscription_created, Signal)