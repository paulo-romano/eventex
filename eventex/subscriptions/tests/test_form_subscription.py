from django.test import TestCase
from eventex.subscriptions.forms import SubscriptionForm

class SubscriptionFormTest(TestCase):
    def test_form_has_fields(self):
        """Form must has fields"""
        self.form = SubscriptionForm()
        expected = ['name', 'cpf', 'email', 'phone']
        self.assertSequenceEqual(expected, list(self.form.fields))

    def test_cpf_digit(self):
        """CPF must accept only digits"""
        form = self.make_validated_form(cpf='ABCD5678901')

        self.assertFormErrorsCode(form, 'cpf', 'digits')

    def test_cpf_has_11_digit(self):
        """CPF must accept only 11 digits"""
        form = self.make_validated_form(cpf=1234)

        self.assertFormErrorsCode(form, 'cpf', 'length')

    def test_name_must_be_capitalized(self):
        """Name must be capitalized"""
        form = self.make_validated_form(name='PAULO romano')
        self.assertEqual('Paulo Romano', form.cleaned_data['name'])

    def test_email_must_be_optional(self):
        """E-mail must be optional"""
        form = self.make_validated_form(email='')

        self.assertFalse(form.errors.get('email'))

    def test_phone_must_be_optional(self):
        """Phone must be optional"""
        form = self.make_validated_form(phone='')

        self.assertFalse(form.errors.get('phone'))

    def test_email_or_phone_must_be_informed(self):
        """E-Mail or Phone must be optional"""
        form = self.make_validated_form(email='', phone='')

        self.assertListEqual(['__all__'], list(form.errors))

    def assertFormErrorsCode(self, form, field, code):
        errors = form.errors.as_data()
        errors_list = errors[field]
        exception  = errors_list[0]

        self.assertEqual(code, exception.code)

    def make_validated_form(self, **kwargs):
        valid = dict(name = 'Paulo Romano', cpf='12345678901',
                    email = 'pauloromanocarvalho@gmail.com',
                    phone = '55-55559999')

        data = dict(valid, **kwargs)

        form = SubscriptionForm(data)
        form.is_valid()

        return form

