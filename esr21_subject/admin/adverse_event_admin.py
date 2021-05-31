from django.contrib import admin
from django.db import models
from django.forms import Textarea

from edc_model_admin import audit_fieldset_tuple
from edc_model_admin.inlines import StackedInlineMixin

from .modeladmin_mixins import CrfModelAdminMixin
from ..forms import AdverseEventForm, SeriousAdverseEventForm
from ..models import AdverseEvent, SeriousAdverseEvent
from ..admin_site import esr21_subject_admin


class SeriousAdverseEventInlineAdmin(StackedInlineMixin, admin.StackedInline):

    model = SeriousAdverseEvent
    form = SeriousAdverseEventForm

    extra = 1
    max_num = 3

    fieldsets = (
        (None, {
            'fields': [
                'start_date',
                'resolution_date',
                'date_aware_of',
                'seriousness_criteria',
                'admission_date',
                'discharge_date',
                'incapacity_specify',
                'medical_event_other',
                'rationale',
                'event_abate',
                'event_reappear',
                'describe_sae_treatmnt',
                'test_performed',
                'additional_info',
                ]}
         ),)

    radio_fields = {'event_abate': admin.VERTICAL,
                    'event_reappear': admin.VERTICAL, }

    filter_horizontal = ('seriousness_criteria', )


@admin.register(AdverseEvent, site=esr21_subject_admin)
class AdverseEventAdmin(CrfModelAdminMixin, admin.ModelAdmin):

    form = AdverseEventForm
    inlines = [SeriousAdverseEventInlineAdmin, ]

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
                'event_details',
                'start_date',
                'status',
                'resolution_date',
                'ae_grade',
                'study_treatmnt_rel',
                'nonstudy_treatmnt_rel',
                'studyproc_treatmnt_rel',
                'action_taken',
                'outcome',
                'sequelae_specify',
                'serious_event',
                'special_interest_ae',
                'medically_attended_ae',
                'maae_specify',
                'treatment_given',
                'ae_study_discontinued',
                'covid_related_ae'
            )
        }),
        audit_fieldset_tuple
    )

    radio_fields = {'status': admin.VERTICAL,
                    'ae_grade': admin.VERTICAL,
                    'study_treatmnt_rel': admin.VERTICAL,
                    'nonstudy_treatmnt_rel': admin.VERTICAL,
                    'studyproc_treatmnt_rel': admin.VERTICAL,
                    'action_taken': admin.VERTICAL,
                    'outcome': admin.VERTICAL,
                    'serious_event': admin.VERTICAL,
                    'special_interest_ae': admin.VERTICAL,
                    'medically_attended_ae': admin.VERTICAL,
                    'treatment_given': admin.VERTICAL,
                    'ae_study_discontinued': admin.VERTICAL,
                    'covid_related_ae': admin.VERTICAL, }


@admin.register(SeriousAdverseEvent, site=esr21_subject_admin)
class SeriousAdverseEventAdmin(admin.ModelAdmin):

    form = SeriousAdverseEventForm

    fieldsets = (
        (None, {
            'fields': [
                'adverse_event',
                'start_date',
                'resolution_date',
                'date_aware_of',
                'seriousness_criteria',
                'admission_date',
                'discharge_date',
                'incapacity_specify',
                'medical_event_other',
                'rationale',
                'event_abate',
                'event_reappear',
                'describe_sae_treatmnt',
                'test_performed',
                'additional_info',
                ]}
         ),)

    radio_fields = {'event_abate': admin.VERTICAL,
                    'event_reappear': admin.VERTICAL, }

    filter_horizontal = ('seriousness_criteria', )
