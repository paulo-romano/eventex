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
    email = forms.EmailField(label='E-Mail')
    phone = forms.CharField(label='Telefone')

    def clean_name(self):
        name = self.cleaned_data['name']
        return ' '.join([name.capitalize() for name in name.split(' ')])