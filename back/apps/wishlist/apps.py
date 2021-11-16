from django.apps import AppConfig


class AnnouncementConfig(AppConfig):
    name = 'apps.announcement'

    def ready(self):
        import apps.announcement.signals
