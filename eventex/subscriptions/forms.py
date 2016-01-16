from django import forms
from django.core.exceptions import ValidationError


def validate_cpf(value):
    if not value.isdigit():
        raise ValidationError('Informe apenas números.', 'digits')

    if len(value) != 11:
        raise ValidationError('CPF deve ter 11 números.', 'length')


class SubscriptionForm(forms.Form):
    name = forms.CharField(label='Nome')
    cpf = forms.CharField(label='CPF', validators=[validate_cpf])
    email = forms.EmailField(label='E-Mail', required=False)
    phone = forms.CharField(label='Telefone', required=False)

    def clean_name(self):
        name = self.cleaned_data['name']
        return ' '.join([name.capitalize() for name in name.split(' ')])

    def clean(self):
        email = self.cleaned_data.get('email')
        phone = self.cleaned_data.get('phone')

        if not email and not phone:
            raise ValidationError('Informe o e-mail ou telefone para contato.')

        return self.cleaned_data
