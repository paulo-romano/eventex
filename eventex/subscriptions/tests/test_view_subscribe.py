from django.core import mail
from django.test import TestCase
from eventex.subscriptions.forms import SubscriptionForm
from eventex.subscriptions.models import Subscription


class SubscribeGet(TestCase):
    def setUp(self):
        self.response = self.client.get('/inscricao/')

    def test_get(self):
        """Get /incricao/ must return status code 200"""
        self.assertEqual(200, self.response.status_code)

    def test_template(self):
        """Must use subscription_form.html template"""
        self.assertTemplateUsed(self.response, 'subscription_form.html')

    def test_html(self):
        """Html must contain input tags"""
        tags = (
            ('<form', 1),
            ('<input', 6),
            ('type="text"', 3),
            ('type="email"', 1),
            ('type="submit"', 1),
        )

        for text, count in tags:
            with self.subTest():
                self.assertContains(self.response, text, count)

    def test_csrf(self):
        """Html must have csrfmiddlewaretoken"""
        self.assertContains(self.response, 'csrfmiddlewaretoken')

    def test_has_form(self):
        """Context must have a form"""
        form = self.response.context['form']
        self.assertIsInstance(form, SubscriptionForm)


class SubscribePostValid(TestCase):
    def setUp(self):
        self.data = dict(name='Paulo Romano', cpf='12345678901',
                    email='pauloromanocarvalho@gmail.com', phone='11-55556666')

        self.response = self.client.post('/inscricao/', self.data)

    def test_post(self):
        """Valid POST should redirect to /inscricao/"""
        self.assertEquals(302, self.response.status_code)
        self.assertRedirects(self.response, '/inscricao/1/')

    def test_send_subscribe_email(self):
        """E-Mail must be sended"""
        self.assertEquals(1, len(mail.outbox))

    def test_save_subscription(self):
        """Must save subscription data"""
        self.assertTrue(Subscription.objects.exists())


class SubscribePostInvalid(TestCase):
    def setUp(self):
        self.response = self.client.post('/inscricao/', {})

    def test_post(self):
        """Invalid POST shouldn't redirect"""
        self.assertEquals(200, self.response.status_code)

    def test_template(self):
        """Must use subscription_form.html template"""
        self.assertTemplateUsed(self.response, 'subscription_form.html')

    def test_has_form(self):
        """Context must have a form"""
        form = self.response.context['form']
        self.assertIsInstance(form, SubscriptionForm)

    def test_for_has_errors(self):
        """Context must have a form"""
        form = self.response.context['form']
        self.assertTrue(form.errors)

    def test_dont_save_subscription(self):
        """Must save subscription data"""
        self.assertFalse(Subscription.objects.exists())
