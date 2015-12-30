from django.shortcuts import render


def subscription(request):
    return render(request, 'subscription_form.html')