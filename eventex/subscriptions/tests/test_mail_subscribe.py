from django.core import mail
from django.test import TestCase
from django.shortcuts import resolve_url

class SubscribeValidPost(TestCase):
    def setUp(self):
        self.data = dict(name='Paulo Romano', cpf='12345678901',
                    email='pauloromanocarvalho@gmail.com', phone='11-55556666')

        self.response = self.client.post(resolve_url('subscriptions:new'), self.data)
        self.email = mail.outbox[0]

    def test_subscription_email_subject(self):
        """E-Mail subject must be equal to expected"""
        expect = 'Confirmação de Inscrição'
        self.assertEqual(expect, self.email.subject)

    def test_subscription_email_from(self):
        """E-Mail to must be equal to informed"""
        expect = 'contato@eventex.com.br'

        self.assertEquals(expect, self.email.from_email)

    def test_subscription_email_to(self):
        """E-Mail to must be equal to informed"""
        expect = ['contato@eventex.com.br', 'pauloromanocarvalho@gmail.com']

        self.assertEquals(expect, self.email.to)

    def test_subscription_email_body(self):
        """E-Mail body must be equal to informed"""
        contents = (
            ('Paulo Romano'),
            ('12345678901'),
            ('pauloromanocarvalho@gmail.com'),
            ('11-55556666'),
        )

        for content in contents:
            with self.subTest():
                self.assertIn(content, self.email.body)