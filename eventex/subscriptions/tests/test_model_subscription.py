from django.test import TestCase
from eventex.subscriptions.models import Subscription
from datetime import datetime


class SubscriptionModelTest(TestCase):
    def setUp(self):
        self.obj = Subscription(
            name = 'Paulo Romano',
            cpf = '12345678901',
            email = 'pauloromanocarvalho@gmail.com',
            phone = '11-55556666',
        )

        self.obj.save()

    def test_create(self):
        """Subscrition must create objects"""
        self.assertTrue(Subscription.objects.exists())

    def test_created_at(self):
        """Subscription must have a automated created_at field"""
        self.assertIsInstance(self.obj.created_at, datetime)

    def test_str(self):
        """Must return self,name"""
        self.assertEqual(str(self.obj), self.obj.name)

    def test_paid_default_False(self):
        """Paid must be False by default"""
        self.assertFalse(self.obj.paid)
