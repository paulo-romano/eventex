from django.test import TestCase

from eventex.subscriptions.models import Subscription


class SubscriptionDetail(TestCase):
    def setUp(self):
        self.obj = Subscription.objects.create(
            name = 'Paulo Romano',
            cpf = '12345678901',
            email = 'pauloromanocarvalho@gmail.com',
            phone = '11-55556666',
        )
        self.response = self.client.get('/inscricao/{0}/'.format(self.obj.pk))

    def test_get(self):
        """Get /incricao/ must return status code 200"""
        self.assertEqual(200, self.response.status_code)

    def test_template(self):
        """Must use subscription_form.html template"""
        self.assertTemplateUsed(self.response, 'subscription_detail.html')

    def test_context(self):
        subscription = self.response.context['subscription']
        self.assertIsInstance(subscription, Subscription)

    def test_html(self):
        contents = (
            self.obj.name,
            self.obj.cpf,
            self.obj.email,
            self.obj.phone,
        )

        for text in contents:
            with self.subTest():
                self.assertContains(self.response, text)


class SubscriptionDetailNotFound(TestCase):
    def test_not_found(self):
        self.response = self.client.get('/inscricao/0/')
        self.assertEqual(404, self.response.status_code)