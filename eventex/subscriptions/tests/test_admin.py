from django.test import TestCase
from eventex.subscriptions.admin import SubscriptionModelAdmin, Subscription, admin
from unittest.mock import Mock


class SubscriptionAdmin(TestCase):
    def setUp(self):
        self.model_admim = SubscriptionModelAdmin(Subscription, admin.site)

        Subscription.objects.create(
            name = 'Paulo Romano',
            cpf = '12345678901',
            email = 'pauloromanocarvalho@gmail.com',
            phone = '11-55556666',
        )


    def test_has_action(self):
        """Admin must have mark_as_paid action"""
        self.assertIn('mark_as_paid', self.model_admim.actions)

    def test_mark_all(self):
        """It should mark all selected subscriptions as paid"""
        self.call_mark_as_paid()
        self.assertEqual(1, Subscription.objects.filter(paid=True).count())

    def test_message(self):
        """mark_as_paid must show a message"""
        mock =  self.call_mark_as_paid()
        mock.assert_called_once_with(None, '1 inscrição foi marcada como paga.')

    def call_mark_as_paid(self):
        mock = Mock()
        old_message_user = self.model_admim.message_user
        self.model_admim.message_user = mock

        queryset = Subscription.objects.all()
        self.model_admim.mark_as_paid(None, queryset)

        self.model_admim.message_user = old_message_user

        return mock