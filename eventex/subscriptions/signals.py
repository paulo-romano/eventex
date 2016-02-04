from django.core.signals import Signal


subscription_created = Signal(providing_args=['name'])