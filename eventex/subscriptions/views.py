from django.shortcuts import render
from eventex.subscriptions.forms import SubscriptionForm


def subscription(request):
    context = {'form': SubscriptionForm()}
    return render(request, 'subscription_form.html', context)