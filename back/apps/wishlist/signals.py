from django.contrib.sites.models import Site
from django.contrib.sites.shortcuts import get_current_site
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from django.utils.translation import ugettext_lazy as _

from apps.account.models import Moderator
from apps.announcement.models import Announcement
from is_coded.utils import MailSender


@receiver(post_save, sender=Announcement)
def on_car_announcement_create(sender, instance, created, **kwargs):
    print('save')

    if created:
        context = {}
        current_site = get_current_site(request=None)
        context['announcement'] = instance
        context['domain'] = current_site.domain
        moderators = [moderator.email for moderator in Moderator.objects.all()]
        MailSender(context, 'moderator_car_announcement.html', _("Yeni Elan"), moderators).send_mail()


@receiver(pre_save, sender=Announcement)
def on_car_announcement_status_change(sender, instance, **kwargs):
    print('pre_save')
    # Previous Value
    announcement = Announcement.objects.filter(id=instance.id).last()
    if announcement is not None:
        if announcement.status != instance.status:
            print('in')
            context = {}
            current_site = get_current_site(request=None)
            context['announcement'] = instance
            context['domain'] = current_site.domain
            emails = [instance.author.email]
            if instance.status == 'active':
                MailSender(context, f'announcement_accepted_notify.html', _("Elanınız Aktiv Olundu"),
                           emails).send_mail()

            if instance.status == 'rejected':
                MailSender(context, f'announcement_rejected_notify.html', _("Elanınınz Qəbul Edilmədi"),
                           emails).send_mail()

    else:
        pass
