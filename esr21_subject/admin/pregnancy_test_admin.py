from django.contrib import admin

from edc_model_admin.model_admin_audit_fields_mixin import audit_fieldset_tuple

from .modeladmin_mixins import CrfModelAdminMixin
from ..forms import PregnancyForm
from ..models import Pregnancy
from ..admin_site import esr21_subject_admin


@admin.register(Pregnancy, site=esr21_subject_admin)
class PregnancyAdmin(CrfModelAdminMixin, admin.ModelAdmin):
    form = PregnancyForm
    fieldsets = (
        (None, {
            'fields': (
                'subject_visit',
                'report_datetime',
                'preg_performed',
                'preg_date',
                'result',)}),
        audit_fieldset_tuple)

    radio_fields = {'preg_performed': admin.VERTICAL,
                    'result': admin.VERTICAL, }
