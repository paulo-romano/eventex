from django.core.mail import send_mail as send
from django.template.loader import render_to_string


def send_mail(subject, from_, to, template_name, context):
    body = render_to_string(template_name, context)
    send(subject, body, from_, [from_, to])
