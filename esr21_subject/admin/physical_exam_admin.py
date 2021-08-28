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
                'abnormalities_found',
                'abn_specify',
                'clinically_significant',
                'participant_weight',
                'participant_height',
                'general_appearance',
                'abnormality_description',
                'face_check',
                'face_description',
                'neck_check',
                'neck_description',
                'respiratory_check',
                'respiratory_description',
                'cardiovascular_check',
                'cardiovascular_description',
                'abdominal_check',
                'abdominal_description',
                'skin_check',
                'skin_description',
                'neurological_check',
                'neurological_description'
            ),
        }),
        audit_fieldset_tuple)

    radio_fields = {'physical_exam': admin.VERTICAL,
                    'abnormalities_found': admin.VERTICAL,
                    'clinically_significant': admin.VERTICAL,
                    'general_appearance': admin.VERTICAL,
                    'face_check': admin.VERTICAL,
                    'neck_check': admin.VERTICAL,
                    'respiratory_check': admin.VERTICAL,
                    'cardiovascular_check': admin.VERTICAL,
                    'abdominal_check': admin.VERTICAL,
                    'skin_check': admin.VERTICAL,
                    'neurological_check': admin.VERTICAL,
                    'reason_not_done': admin.VERTICAL, }
