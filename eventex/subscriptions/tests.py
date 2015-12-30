from django.test import TestCase

class SubscribeTest(TestCase):
    def setUp(self):
        self.response = self.client.get('/inscricao/')

    def test_get(self):
        """ Get /incricao/ must return status code 200 """
        self.assertEqual(200, self.response.status_code)

    def test_template(self):
        """ Must use subscription_form.html template """
        self.assertTemplateUsed(self.response, 'subscription_form.html')

    def test_form_action(self):
        """ template must have a form with action post """
        self.assertContains(self.response, 'form action="." method="post"')

    def test_textfield_name(self):
        """ template must have name text field """
        self.assertContains(self.response, 'type="text" name="name"')

    def test_textfield_cpf(self):
        """ template must have cpf text field """
        self.assertContains(self.response, 'type="text" name="cpf"')

    def test_textfield_email(self):
        """ template must have email text field """
        self.assertContains(self.response, 'type="text" name="email"')

    def test_textfield_phone(self):
        """ template must have phone text field """
        self.assertContains(self.response, 'type="text" name="phone"')

    def test_submitfield_enviar(self):
        """ template must have a Enviar button """
        self.assertContains(self.response, 'type="submit" value="Enviar"')

    def test_csrf(self):
        """ Html must have csrfmiddlewaretoken """
        self.assertContains(self.response, 'csrfmiddlewaretoken')