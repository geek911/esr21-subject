from django.contrib import admin
from django.db import models
from django.forms import Textarea
from edc_model_admin import audit_fieldset_tuple
from edc_model_admin.inlines import StackedInlineMixin

from .modeladmin_mixins import CrfModelAdminMixin
from ..forms import AdverseEventForm, AdverseEventRecordForm
from ..models import AdverseEvent, AdverseEventRecord
from ..admin_site import esr21_subject_admin


class AdverseEventRecordInlineAdmin(StackedInlineMixin, admin.StackedInline):
    model = AdverseEventRecord
    form = AdverseEventRecordForm

    extra = 0

    fieldsets = (
        (None, {
            'fields': [
                'ae_number',
                'ae_term',
                'ae_details',
                'start_date',
                'stop_date',
                'substance_hypersensitivity',
                'study_treatmnt_rel',
                'nonstudy_treatmnt_rel',
                'studyproc_treatmnt_rel',
                'outcome',
                'sequelae_specify',
                'serious_event',
                'investigation_product',
                'action_taken',
                'special_interest_ae',
                'medically_attended_ae',
                'maae_specify',
                'hospitalized',
                'treatment_given',
                'treatmnt_given_specify',
                'ae_study_discontinued',
                'discontn_dt',
                'covid_related_ae',
                'ae_rel',
                'llt_code',
                'llt_name',
                'pt_code',
                'pt_name',
                'hlt_code',
                'hlt_name',
                'hlgt_code',
                'hlgt_name',
                'soc_code',
                'soc_name',
                'meddra_v',
                'ctcae_v'

            ]}
        ),)

    radio_fields = {
        'study_treatmnt_rel': admin.VERTICAL,
        'nonstudy_treatmnt_rel': admin.VERTICAL,
        'studyproc_treatmnt_rel': admin.VERTICAL,
        'action_taken': admin.VERTICAL,
        'outcome': admin.VERTICAL,
        'serious_event': admin.VERTICAL,
        'special_interest_ae': admin.VERTICAL,
        'medically_attended_ae': admin.VERTICAL,
        'hospitalized' : admin.VERTICAL,
        'treatment_given': admin.VERTICAL,
        'ae_study_discontinued': admin.VERTICAL,
        'substance_hypersensitivity': admin.VERTICAL,
        'covid_related_ae': admin.VERTICAL,
        'ae_rel': admin.VERTICAL,
        }


@admin.register(AdverseEvent, site=esr21_subject_admin)
class AdverseEventAdmin(CrfModelAdminMixin, admin.ModelAdmin):
    form = AdverseEventForm
    inlines = [AdverseEventRecordInlineAdmin, ]

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
            )
        }),
        audit_fieldset_tuple
    )

    radio_fields = {'experienced_ae': admin.VERTICAL, }

    def render_change_form(self, request, context, add=False, change=False, form_url='', obj=None):
        context.update({
            'show_save': True,
            'show_save_and_continue': False,
            'show_save_and_add_another': False,
            'show_delete': True
        })
        return super().render_change_form(request, context, add, change, form_url, obj)
