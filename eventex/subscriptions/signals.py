from django.core.signals import Signal
from django.dispatch import receiver
from django.core.mail import send_mail

subscription_created = Signal(providing_args=['name'])


@receiver(subscription_created)
def send_warning_admin(sender, **kwargs):
    send_mail('Nova Inscrição', '{} acaba de se inscrever!'.format(kwargs.get('name')), 'pauloromanocarvalho@gmail.com', ['pauloromanocarvalho@gmail.com'])