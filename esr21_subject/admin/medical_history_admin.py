from django.contrib import admin

from .modeladmin_mixins import CrfModelAdminMixin
from ..forms import MedicalHistoryForm
from ..models import MedicalHistory
from ..admin_site import esr21_subject_admin


@admin.register(MedicalHistory, site=esr21_subject_admin)
class MedicalHistoryAdmin(CrfModelAdminMixin, admin.ModelAdmin):
    form = MedicalHistoryForm

    fieldsets = (
        (None, {
            'fields': (
                'subject_visit',
                'report_datetime',
                'relevant_history',
                'was_subject_infected_before',
                'symptoms',
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
    )

    radio_fields = {
        'relevant_history': admin.VERTICAL,
        'was_subject_infected_before': admin.VERTICAL,
        'smoking_status': admin.VERTICAL,
        'alcohol_status': admin.VERTICAL,
        'diabetes': admin.VERTICAL,
        'mode_of_transport': admin.VERTICAL,
        'using_shared_kitchen': admin.VERTICAL,
    }

    filter_horizontal = ('symptoms', 'comorbidities')
