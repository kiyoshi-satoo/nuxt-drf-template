from django.contrib import admin
from django.db import models
from django.contrib.admin.widgets import AdminFileWidget
from django.utils.html import format_html
from django.utils.safestring import mark_safe
from django.utils.translation import ugettext_lazy as _
# Register your models here.
from apps.announcement.models import Announcement, AnnouncementImage, Option, Brand, Color, CarModel, BanType, FuelType, \
    TransmissionType, \
    DriveType, AnnouncementView
from core.forms import AtLeastOneImageFormSet
from core.models import City

admin.site.register(Color)
admin.site.register(Brand)
admin.site.register(CarModel)
admin.site.register(BanType)
admin.site.register(FuelType)
admin.site.register(TransmissionType)
admin.site.register(DriveType)
admin.site.register(Option)
admin.site.register(City)
admin.site.register(AnnouncementView)


class ImageHaveAnnouncementFilter(admin.SimpleListFilter):
    # Human-readable title which will be displayed in the
    # right admin sidebar just above the filter options.
    title = _('Elana baglananlar')

    # Parameter for the filter that will be used in the URL query.
    parameter_name = 'announcement_have'

    def lookups(self, request, model_admin):
        return (
            ('+', _('Have an announcement')),
            ('-', _("Don't have")),
        )

    def queryset(self, request, queryset):
        if self.value() == '+':
            return queryset.filter(announcement__isnull=False)
        if self.value() == '-':
            return queryset.filter(announcement__isnull=True)


@admin.register(AnnouncementImage)
class AnnouncementImageAdmin(admin.ModelAdmin):
    list_display = ('announcement',)
    list_filter = (ImageHaveAnnouncementFilter, 'created_date',)


class AdminImageWidget(AdminFileWidget):
    def render(self, name, value, attrs=None, renderer=None):
        output = []
        if value and getattr(value, "url", None):
            image_url = value.url
            file_name = str(value)
            output.append(
                u' <a href="%s" target="_blank"><img src="%s" alt="%s" width="150" height="150"  style="object-fit: cover;"/></a> %s ' % \
                (image_url, image_url, file_name, _('')))
        output.append(super(AdminFileWidget, self).render(name, value, attrs))
        return mark_safe(u''.join(output))


class AnnouncementImageInline(admin.TabularInline):
    model = AnnouncementImage
    formset = AtLeastOneImageFormSet
    formfield_overrides = {models.ImageField: {'widget': AdminImageWidget}}
    extra = 1


@admin.register(Announcement)
class AnnouncementAdmin(admin.ModelAdmin):
    empty_value_display = '-empty-'
    inlines = [AnnouncementImageInline]
    radio_fields = {'currency': admin.HORIZONTAL}

    fieldsets = (
        (
            None,
            {
                'fields': (
                    ('key',), ('slug',)
                )
            }
        ),
        (
            _('Elan Sahibi Məlumatları'),
            {
                'fields': (
                    ('author',)
                )
            }
        ),
        (
            _('Əsas Məlumatlar'),
            {
                'fields': (
                    ('brand', 'fuel_type',), ('model', 'drive_type',),
                    ('ban_type', 'transmission_type',),
                    ('mileage', 'release_date'),
                    ('color', 'engine_volume',),
                    ('price', 'currency', 'engine_power'),
                    ('options',),
                )
            }
        ),
        (
            _('Əlavə Məlumatlar'),
            {
                'fields': (
                    ('description',), ('is_vip', 'status', 'rejected_reason'), ('on_barter', 'on_credit',)
                )
            }
        ),
    )
    # The forms to add and change user instances
    list_display = ('is_vip', 'author', 'brand', 'model', 'release_date', 'image_tag')
    list_filter = ('is_vip', 'release_date',)
    search_fields = ('brand', 'model', 'author')
    readonly_fields = ('key',)
    ordering = ('-date_created',)

    def image_tag(self, obj):
        if (obj.thumb_image):
            return format_html('<img src="{0}" style="width: 70px; height:70px;" />'.format(obj.thumb_image.image.url))
        else:
            return None

    class Media:
        js = ('/static/js/admin.js',)
