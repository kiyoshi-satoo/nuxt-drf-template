import datetime
import secrets

from django.contrib.auth.tokens import default_token_generator
from django.core.mail import EmailMessage
from django.core.validators import MaxValueValidator
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode
from unidecode import unidecode


def key_generator():
    generated_key = secrets.token_urlsafe(12)

    return generated_key


def current_year():
    return datetime.date.today().year


def max_value_current_year(value):
    return MaxValueValidator(current_year())(value)


# Custom slugify function
def slugify(title):
    symbol_mapping = (
        (' ', '-'),
        ('.', '-'),
        (',', '-'),
        ('!', '-'),
        ('?', '-'),
        ("'", '-'),
        ('"', '-'),
        ('ə', 'e'),
        ('ı', 'i'),
        ('İ', 'i'),
        ('i', 'i'),
        ('ö', 'o'),
        ('ğ', 'g'),
        ('ü', 'u'),
        ('ş', 's'),
        ('ç', 'c'),
    )
    title_url = title.strip().lower()

    for before, after in symbol_mapping:
        title_url = title_url.replace(before, after)

    return unidecode(title_url)


def send_mail(current_site, subject, user, to_email, template):
    mail_subject = subject
    message = render_to_string(f'Mail/{template}', {
        'user': user,
        'domain': current_site.domain,
        'uid': urlsafe_base64_encode(force_bytes(user.pk)),
        'token': default_token_generator.make_token(user),
    })
    email = EmailMessage(
        mail_subject, message, to=[to_email]
    )
    email.send()


def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip


def get_or_none(classmodel, **kwargs):
    try:
        return classmodel.objects.get(**kwargs)
    except classmodel.DoesNotExist:
        return None


class MailSender:

    def __init__(self, context, template, subject, to_email):
        from apps.base_user.models import MyUser

        self.to_email = to_email
        self.context = context
        self.template = template
        self.subject = subject
        self.from_email = "info@efgroup.az"

    #
    # def indirect_notify(self, status, instance):
    #     method_name = 'notify_' + str(status).lower()
    #     print(f'STATUS:{method_name}')
    #     method = getattr(self, method_name, lambda: 'Invalid')
    #     return method(instance)

    def send_mail(self):
        from django.core.mail import EmailMultiAlternatives
        from django.template.loader import render_to_string
        from django.utils.html import strip_tags
        print('sending email')
        html_content = render_to_string(f'Mail/{self.template}', self.context)
        text_content = strip_tags(html_content)
        msg = EmailMultiAlternatives(self.subject, text_content, self.from_email, to=self.to_email)
        msg.attach_alternative(html_content, "text/html")
        msg.send()
        print('Successfully sent')
