def slugify(title):
    from unidecode import unidecode
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


class MailAdmin:

    def __init__(self, context, template, subject):
        from apps.base_user.models import MyUser

        self.to_email = [admin.email for admin in MyUser.objects.filter(is_superuser=True).all()],
        self.context = context
        self.template = template
        self.subject = subject
        self.from_email = "info@ibay.az"

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
        msg = EmailMultiAlternatives(self.subject, text_content, self.from_email, to=self.to_email[0])
        msg.attach_alternative(html_content, "text/html")
        msg.send()
        print('Successfully sent')
