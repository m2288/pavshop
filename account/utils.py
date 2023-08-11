from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes
from django.contrib.sites.shortcuts import get_current_site
from .tokens import account_activation_token


def send_activation_email(request, user):
    current_site = get_current_site(request)
    subject = 'Activate Your Pavshop Account'
    message = render_to_string('account/account_activation_email.html', {
        'user': user,
        'domain': current_site.domain,
        'uid': urlsafe_base64_encode(force_bytes(user.pk)),
        'token': account_activation_token.make_token(user),
    })
    email = EmailMessage(subject, message, to=[user.email])
    email.content_subtype = 'html'  # Set the content type as HTML
    email.send()
