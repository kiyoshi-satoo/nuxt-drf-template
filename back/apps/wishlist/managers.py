from django.db import models


class AnnouncementQuerySet(models.QuerySet):
    def is_active(self):
        return self.filter(status='active')

    def is_pending(self):
        return self.filter(status='pending')

    def is_vip(self):
        return self.filter(is_vip=True, status='active')

    def is_regular(self):
        return self.filter(is_vip=False, status='active')


class AnnouncementManager(models.Manager):

    def get_queryset(self):
        return AnnouncementQuerySet(self.model, using=self._db)

    def is_active(self):
        return self.get_queryset().is_active()

    def is_pending(self):
        return self.get_queryset().is_pending()

    def is_vip(self):
        return self.get_queryset().is_vip()

    def is_regular(self):
        return self.get_queryset().is_regular()
