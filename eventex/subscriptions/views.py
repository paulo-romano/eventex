from django.conf import settings
from django.http import Http404
from django.shortcuts import render, redirect, resolve_url
from eventex.subscriptions.forms import SubscriptionForm
from eventex.subscriptions.models import Subscription
from eventex.subscriptions.services import send_mail
from eventex.subscriptions.signals import subscription_created


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

        send_mail('Confirmação de Inscrição', settings.DEFAULT_FROM_EMAIL, subscription.email,
                   'subscription_email.txt', {'subscription': subscription})

        subscription_created.send(sender=create, name=subscription.name)

        return redirect(resolve_url('subscriptions:detail', subscription.pk))


def empty_form(request):
    return render(request, 'subscription_form.html', {'form': SubscriptionForm()})
