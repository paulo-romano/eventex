from django.core.mail import send_mail
from django.contrib import messages
from django.shortcuts import render, redirect
from django.template.loader import render_to_string
from django.conf import settings
from eventex.subscriptions.forms import SubscriptionForm


def subscribe(request):
    if request.method == 'POST':
        return create(request)
    else:
        return new(request)


def create(request):
    form = SubscriptionForm(request.POST)

    if not form.is_valid():
        return render(request, 'subscription_form.html', {'form': form})

    else:
        _send_mail('Confirmação de Inscrição', settings.DEFAULT_FROM_EMAIL, form.cleaned_data['email'],
                   'subscription_email.txt', form.cleaned_data)

        messages.success(request, 'Inscrição realizada com sucesso!')

        return redirect('/inscricao/')


def new(request):
    return render(request, 'subscription_form.html', {'form': SubscriptionForm()})


def _send_mail(subject, from_, to, template_name, context):
    body = render_to_string(template_name, context)
    send_mail(subject, body, from_, [from_, to])