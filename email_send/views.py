from django.shortcuts import redirect
from django.template.loader import render_to_string
from django.core.mail import EmailMultiAlternatives
from django.utils.html import strip_tags
from django.conf import settings
from django.views.decorators.http import require_GET

@require_GET
def email_newsletter(request):

    email_user = request.GET.get('email_user')

    html_content = render_to_string('email_html/newsletter.html')
    text_content = strip_tags(html_content)

    Email = EmailMultiAlternatives(
    'Teste de email - EULER',
    text_content,
    settings.EMAIL_HOST_USER,
    [str(email_user),],
    )
    Email.attach_alternative(html_content, 'text/html')
    Email.send()

    return redirect(request.META.get('HTTP_REFERER'))


