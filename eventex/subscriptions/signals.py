from django.core.signals import Signal
from django.dispatch import receiver

subscription_created = Signal(providing_args=['name'])


@receiver(subscription_created)
def send_warning_admin(sender, **kwargs):
    pass