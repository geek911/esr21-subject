from django.contrib import admin

from edc_model_admin.model_admin_audit_fields_mixin import audit_fieldset_tuple

from .modeladmin_mixins import CrfModelAdminMixin
from ..forms import PregnancyTestForm
from ..models import PregnancyTest
from ..admin_site import esr21_subject_admin


@admin.register(PregnancyTest, site=esr21_subject_admin)
class PregnancyTestAdmin(CrfModelAdminMixin, admin.ModelAdmin):
    form = PregnancyTestForm
    fieldsets = (
        (None, {
            'fields': (
                'subject_visit',
                'report_datetime',
                'preg_performed',
                'preg_test_type',
                'preg_date',
                'result',)}),
        audit_fieldset_tuple)

    radio_fields = {'preg_performed': admin.VERTICAL,
                    'preg_test_type': admin.VERTICAL,
                    'result': admin.VERTICAL, }
