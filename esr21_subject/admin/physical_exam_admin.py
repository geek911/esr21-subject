from django.contrib import admin
from django.db import models
from django.forms import Textarea

from edc_model_admin.model_admin_audit_fields_mixin import audit_fieldset_tuple

from .modeladmin_mixins import CrfModelAdminMixin
from ..forms import PhysicalExamForm
from ..models import PhysicalExam
from ..admin_site import esr21_subject_admin


@admin.register(PhysicalExam, site=esr21_subject_admin)
class PhysicalExamAdmin(CrfModelAdminMixin, admin.ModelAdmin):
    form = PhysicalExamForm

    formfield_overrides = {
        models.TextField: {'widget': Textarea(
            attrs={'rows': 500,
                   'cols': 70,
                   'style': 'height: 7em;'})},
    }
    fieldsets = (
        (None, {
            'fields': (
                'subject_visit',
                'report_datetime',
                'physical_exam',
                'reason_not_done',
                'exam_date',
                'abnormalities',
                'abn_specify',
                'clinically_significant',
                'comment',
            ),
        }),
        audit_fieldset_tuple)

    radio_fields = {'physical_exam': admin.VERTICAL,
                    'abnormalities': admin.VERTICAL,
                    'clinically_significant': admin.VERTICAL,
                    'reason_not_done': admin.VERTICAL, }
