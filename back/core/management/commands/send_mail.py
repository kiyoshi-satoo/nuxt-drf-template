from decouple import config
from django.core.mail import send_mail
from django.core.management import BaseCommand


class Command(BaseCommand):
    help = "This is send test mail command"

    def handle(self, *args, **options):
        print("Start")

        send_mail(
            'Hi',
            'This is send test mail command',
            config('EMAIL_HOST_USER'),
            ['to_mail@gmail.com'],
            fail_silently=False,
        )
        print("DONE")
