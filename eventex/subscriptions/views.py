from django.core.mail import send_mail
from django.contrib import messages
from django.shortcuts import render, redirect
from django.template.loader import render_to_string

from eventex.subscriptions.forms import SubscriptionForm


def subscription(request):
    if request.method == 'POST':

        form = SubscriptionForm(request.POST)

        if form.is_valid():

            body = render_to_string('subscription_email.txt', form.cleaned_data)

            send_mail('Confirmação de Inscrição',
                      body,
                      'contato@eventex.com.br',
                      [form.cleaned_data['email'], 'contato@eventex.com.br'])

            messages.success(request, 'Inscrição realizada com sucesso!')

            return redirect('/inscricao/')

        else:
            return render(request, 'subscription_form.html', {'form': form})

    else:
        context = {'form': SubscriptionForm()}
        return render(request, 'subscription_form.html', context)
