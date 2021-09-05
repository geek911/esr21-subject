from django.contrib import admin
from django.db import models
from django.forms import Textarea

from edc_model_admin import audit_fieldset_tuple
from edc_model_admin.inlines import StackedInlineMixin

from .modeladmin_mixins import CrfModelAdminMixin
from ..forms import AdverseEventForm, SeriousAdverseEventForm
from ..forms import SpecialInterestAdverseEventForm
from ..models import AdverseEvent, SeriousAdverseEvent
from ..models import SpecialInterestAdverseEvent
from ..admin_site import esr21_subject_admin


class SeriousAdverseEventInlineAdmin(StackedInlineMixin, admin.StackedInline):

    model = SeriousAdverseEvent
    form = SeriousAdverseEventForm

    extra = 0
    max_num = 3

    fieldsets = (
        (None, {
            'fields': [
                'sae_name',
                'meddra_pname',
                'meddra_pcode',
                'meddra_version',
                'sae_details',
                'sae_intensity',
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
                'describe_sae_treatmnt',
                'test_performed',
                'additional_info',
            ]}
         ),)

    radio_fields = {'sae_intensity': admin.VERTICAL,
                    'event_abate': admin.VERTICAL, }

    filter_horizontal = ('seriousness_criteria',)


class SpecialInterestAdverseEventInlineAdmin(StackedInlineMixin,
                                             admin.StackedInline):

    model = SpecialInterestAdverseEvent
    form = SpecialInterestAdverseEventForm

    extra = 0
    max_num = 3

    fieldsets = (
        ('Participants should be encouraged to report any adverse events reported in '
         'the AE form', {
             'fields': [
                 'aesi_name',
                 'meddra_pname',
                 'meddra_pcode',
                 'meddra_version',
                 'start_date',
                 'end_date',
                 'date_aware_of',
                 'aesi_category',
                 'rationale',
                 'describe_aesi_treatmnt',
                 'additional_info',
             ]}
         ),)

    radio_fields = {
        'aesi_category': admin.VERTICAL,
    }


@admin.register(AdverseEvent, site=esr21_subject_admin)
class AdverseEventAdmin(CrfModelAdminMixin, admin.ModelAdmin):

    form = AdverseEventForm
    inlines = [SeriousAdverseEventInlineAdmin,
               SpecialInterestAdverseEventInlineAdmin]

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
                'experienced_ae',
                'ae_name',
                'meddra_pname',
                'meddra_pcode',
                'meddra_version',
                'event_details',
                'start_date',
                'stop_date',
                'substance_hypersensitivity',
                'status',
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
                'treatmnt_given_specify',
                'ae_study_discontinued',
                'discontn_dt',
                'covid_related_ae'
            )
        }),
        audit_fieldset_tuple
    )

    radio_fields = {'experienced_ae': admin.VERTICAL,
                    'status': admin.VERTICAL,
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
                    'substance_hypersensitivity': admin.VERTICAL,
                    'covid_related_ae': admin.VERTICAL, }


@admin.register(SeriousAdverseEvent, site=esr21_subject_admin)
class SeriousAdverseEventAdmin(admin.ModelAdmin):

    form = SeriousAdverseEventForm

    fieldsets = (
        (None, {
            'fields': (
                'adverse_event',
                'sae_name',
                'meddra_pname',
                'meddra_pcode',
                'meddra_version',
                'sae_details',
                'sae_intensity',
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
                'describe_sae_treatmnt',
                'test_performed',
                'additional_info',
            ),
        }),
    )

    radio_fields = {'sae_intensity': admin.VERTICAL,
                    'event_abate': admin.VERTICAL, }

    filter_horizontal = ('seriousness_criteria',)


@admin.register(SpecialInterestAdverseEvent, site=esr21_subject_admin)
class SpecialInterestAdverseEventAdmin(admin.ModelAdmin):

    form = SpecialInterestAdverseEventForm

    extra = 0
    max_num = 3

    fieldsets = (
        (None, {
            'fields': (
                'adverse_event',
                'aesi_name',
                'meddra_pname',
                'meddra_pcode',
                'meddra_version',
                'start_date',
                'end_date',
                'date_aware_of',
                'aesi_category',
                'rationale',
                'describe_aesi_treatmnt',
                'additional_info',
            ),
        }),
    )

    radio_fields = {'aesi_category': admin.VERTICAL, }
