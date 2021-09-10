from django.contrib import admin
from .modeladmin_mixins import CrfModelAdminMixin
from edc_model_admin.inlines import StackedInlineMixin
from edc_model_admin import audit_fieldset_tuple

from ..forms import MedicalHistoryForm, MedicalDiagnosisForm
from ..models import MedicalHistory, MedicalDiagnosis
from ..admin_site import esr21_subject_admin


class MedicalDiagnosisInlineAdmin(StackedInlineMixin, admin.StackedInline):

    model = MedicalDiagnosis
    form = MedicalDiagnosisForm

    extra = 0
    max_num = 3

    fieldsets = (
        (None, {
            'fields': [
                'medical_history',
                'start_date',
                'end_date',
                'ongoing',
                'condition_related_meds',
                'rel_conc_meds',
            ]}
         ),)

    radio_fields = {
        'ongoing': admin.VERTICAL,
        'condition_related_meds': admin.VERTICAL,
    }


@admin.register(MedicalHistory, site=esr21_subject_admin)
class MedicalHistoryAdmin(CrfModelAdminMixin, admin.ModelAdmin):
    form = MedicalHistoryForm

    inlines = [MedicalDiagnosisInlineAdmin]

    fieldsets = (
        (None, {
            'fields': (
                'subject_visit',
                'report_datetime',
                'pregnancy_status',
                'thrombosis_or_thrombocytopenia',
                'clinical_bleeding',
                'guillain_barre_syndrome',
                'suspected_immuno_condition',
                'relevant_history',
                'prior_covid_infection',
                'covid_symptoms',
                'symptoms_other',
                'smoking_status',
                'alcohol_status',
                'diabetes',
                'comorbidities',
                'comorbidities_other',
                'no_of_mass_gathering',
                'no_internal_trips',
                'mode_of_transport',
                'using_shared_kitchen',
            ),
        }),
        audit_fieldset_tuple
    )

    radio_fields = {
        'pregnancy_status': admin.VERTICAL,
        'prior_covid_infection': admin.VERTICAL,
        'smoking_status': admin.VERTICAL,
        'alcohol_status': admin.VERTICAL,
        'diabetes': admin.VERTICAL,
        'mode_of_transport': admin.VERTICAL,
        'using_shared_kitchen': admin.VERTICAL,
        'thrombosis_or_thrombocytopenia': admin.VERTICAL,
        'clinical_bleeding': admin.VERTICAL,
        'guillain_barre_syndrome': admin.VERTICAL,
        'suspected_immuno_condition': admin.VERTICAL,
        'relevant_history': admin.VERTICAL,
    }

    filter_horizontal = ('covid_symptoms', 'comorbidities')
