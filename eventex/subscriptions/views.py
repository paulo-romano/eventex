from django.conf import settings
from django.core.mail import send_mail
from django.http import Http404
from django.shortcuts import render, redirect, resolve_url
from django.template.loader import render_to_string

from eventex.subscriptions.forms import SubscriptionForm
from eventex.subscriptions.models import Subscription


def new(request):
    if request.method == 'POST':
        return create(request)
    else:
        return empty_form(request)


def detail(request, pk):
    try:
        subscription = Subscription.objects.get(pk=pk)
    except Subscription.DoesNotExist:
        raise Http404

    return render(request, 'subscription_detail.html', {'subscription': subscription})


def create(request):
    form = SubscriptionForm(request.POST)

    if not form.is_valid():
        return render(request, 'subscription_form.html', {'form': form})

    else:
        subscription = Subscription.objects.create(**form.cleaned_data)

        _send_mail('Confirmação de Inscrição', settings.DEFAULT_FROM_EMAIL, subscription.email,
                   'subscription_email.txt', {'subscription': subscription})

        return redirect(resolve_url('subscriptions:detail', subscription.pk))


def empty_form(request):
    return render(request, 'subscription_form.html', {'form': SubscriptionForm()})


def _send_mail(subject, from_, to, template_name, context):
    body = render_to_string(template_name, context)
    send_mail(subject, body, from_, [from_, to])
