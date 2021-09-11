from django.contrib import admin

from edc_model_admin.model_admin_audit_fields_mixin import audit_fieldset_tuple

from .modeladmin_mixins import ModelAdminMixin
from ..forms import ScreeningEligibilityForm
from ..models import ScreeningEligibility
from ..admin_site import esr21_subject_admin


@admin.register(ScreeningEligibility, site=esr21_subject_admin)
class ScreeningEligibilityAdmin(ModelAdminMixin, admin.ModelAdmin):

    form = ScreeningEligibilityForm

    fieldsets = (
        (None, {
            'fields': (
                'subject_identifier',
                'report_datetime',
                'covid_symptoms',
                'symptoms_other',
                'comorbidities',
                'pregnancy_status',
                'thrombosis_or_thrombocytopenia',
                'guillain_barre_syndrome',
                'suspected_immuno_condition',
                'clinical_bleeding'
            )}),
        audit_fieldset_tuple)

    radio_fields = {
        'pregnancy_status': admin.VERTICAL,
        'thrombosis_or_thrombocytopenia': admin.VERTICAL,
        'guillain_barre_syndrome': admin.VERTICAL,
        'suspected_immuno_condition': admin.VERTICAL,
        'clinical_bleeding': admin.VERTICAL,
    }

    filter_horizontal = ('covid_symptoms', 'comorbidities')
