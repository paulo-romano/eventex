from django.core import mail
from django.test import TestCase
from eventex.subscriptions.forms import SubscriptionForm

class SubscribeTest(TestCase):
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
        self.assertContains(self.response, '<form')
        self.assertContains(self.response, '<input', 6)
        self.assertContains(self.response, 'type="text"', 3)
        self.assertContains(self.response, 'type="email"')
        self.assertContains(self.response, 'type="submit"')

    def test_csrf(self):
        """Html must have csrfmiddlewaretoken"""
        self.assertContains(self.response, 'csrfmiddlewaretoken')

    def test_has_form(self):
        """Context must have a form"""
        form = self.response.context['form']
        self.assertIsInstance(form, SubscriptionForm)

    def test_form_has_fields(self):
        """Form must has fields"""
        form = self.response.context['form']
        self.assertSequenceEqual(['name', 'cpf', 'email', 'phone'], list(form.fields))


class SubscribePostTest(TestCase):
    def setUp(self):
        self.data = dict(name='Paulo Romano', cpf='12345678901',
                    email='pauloromanocarvalho@gmail.com', phone='11-55556666')

        self.response = self.client.post('/inscricao/', self.data)

    def test_post(self):
        """Valid POST should redirect to /inscricao/"""
        self.assertEquals(302, self.response.status_code)

    def test_send_subscribe_email(self):
        """E-Mail must be sended"""
        self.assertEquals(1, len(mail.outbox))

    def test_subscription_email_subject(self):
        """E-Mail subject must be equal to expected"""
        email = mail.outbox[0]
        expect = 'Confirmação de Inscrição'

        self.assertEqual(expect, email.subject)

    def test_subscription_email_from(self):
        """E-Mail to must be equal to informed"""
        email = mail.outbox[0]
        expect = 'contato@eventex.com.br'

        self.assertEquals(expect, email.from_email)

    def test_subscription_email_to(self):
        """E-Mail to must be equal to informed"""
        email = mail.outbox[0]
        expect = ['pauloromanocarvalho@gmail.com', 'contato@eventex.com.br']

        self.assertEquals(expect, email.to)

    def test_subscription_email_body(self):
        """E-Mail body must be equal to informed"""
        email = mail.outbox[0]

        self.assertIn('Paulo Romano', email.body)
        self.assertIn('12345678901', email.body)
        self.assertIn('pauloromanocarvalho@gmail.com', email.body)
        self.assertIn('11-55556666', email.body)


class SubscribeInvalidPostTest(TestCase):
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


class SubscribeSucessMessage(TestCase):
    def test_message(self):
        self.data = dict(name='Paulo Romano', cpf='12345678901',
                    email='pauloromanocarvalho@gmail.com', phone='11-55556666')
        self.response = self.client.post('/inscricao/', self.data, follow=True)
        self.assertContains(self.response, 'Inscrição realizada com sucesso')